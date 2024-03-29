import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

import click
import time
import json
import re
from flask import Flask, request, url_for, g, redirect
from app.libs.utils import common_render, redirect_back_url
from app.models.user import User
from flask_login import current_user

from app.extensions import login_manager, db, csrf, migrate
from app.exceptions.base import APIException, HTTPException, UnknownException, WebException

from app.libs.utils import ep_meta, route_meta_infos


def create_app(environment='development'):
    app = Flask(__name__, static_url_path='/', static_folder='templates')
    app.config['ENV'] = environment
    env = app.config.get('ENV')

    if env == 'production':
        app.config.from_object('app.config.setting.ProductionConfig')
        app.config.from_object('app.config.secure.ProductionSecure')
    elif env == 'development':
        app.config.from_object('app.config.setting.DevelopmentConfig')
        app.config.from_object('app.config.secure.DevelopmentSecure')
    app.config.from_object('app.config.log')

    from app.libs.Helper import Helper
    app.add_template_global(Helper)

    register_extensions(app)
    register_commands(app)
    register_shell_context(app)
    register_blueprints(app)
    register_errors(app)

    register_before_request(app)
    register_after_request(app)

    mount_router(app)

    return app


def mount_router(app):
    for ep, func in app.view_functions.items():
        info = route_meta_infos.get(func.__name__ + str(func.__hash__()), None)
        if info:
            ep_meta.setdefault(ep, info)


def register_before_request(app):
    @app.before_request
    def request_cost_time():
        g.request_start_time = time.time()
        g.request_time = lambda: "%.5f" % (time.time() - g.request_start_time)

    @app.before_request
    def request_no_auth():
        url = request.path
        login_url = url_for('cms.user+login')
        if not current_user.is_authenticated and url != login_url and not re.match('.*(?:css|less|js|png|jpg)$', url):
            return redirect(login_url)


def register_after_request(app):
    @app.after_request
    def log_response(resp):
        log_config = app.config.get('LOG')
        if not log_config['REQUEST_LOG']:
            return resp
        message = f'[{request.method}] -> [{request.path}] from:{request.remote_addr} costs:{float(g.request_time()) * 1000:.2f} ms '
        if log_config['LEVEL'] == 'INFO':
            app.logger.info(message)
        elif log_config['LEVEL'] == 'DEBUG':
            req_body = '{}'
            try:
                req_body = request.get_json() if request.get_json() else {}
            except:
                pass
            message += " data:{\n\tparam: %s, \n\tbody: %s\n} " % (
                json.dumps(request.args, ensure_ascii=False),
                req_body
            )
            app.logger.debug(message)
        return resp


# def register_logging(app):
#     class RequestFormatter(logging.Formatter):
#
#         def format(self, record):
#             record.url = request.url
#             record.remote_addr = request.remote_addr
#             return super(RequestFormatter, self).format(record)
#
#     request_formatter = RequestFormatter(
#         '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
#         '%(levelname)s in %(module)s: %(message)s'
#     )
#
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     file_handler = RotatingFileHandler(os.path.join(basedir, 'logs/bluelog.log'),
#                                        maxBytes=10 * 1024 * 1024, backupCount=10)
#     file_handler.setFormatter(formatter)
#     file_handler.setLevel(logging.INFO)
#
#     mail_handler = SMTPHandler(
#         mailhost=app.config['MAIL_SERVER'],
#         fromaddr=app.config['MAIL_USERNAME'],
#         toaddrs=['ADMIN_EMAIL'],
#         subject='Bluelog Application Error',
#         credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))
#     mail_handler.setLevel(logging.ERROR)
#     mail_handler.setFormatter(request_formatter)
#
#     if not app.debug:
#         app.logger.addHandler(mail_handler)
#         app.logger.addHandler(file_handler)

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from app.blueprints.cms import cms_bp
    from app.blueprints.home import home_bp
    from app.blueprints.demo import demo_bp
    app.register_blueprint(cms_bp, url_prefix='/cms')
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(demo_bp, url_prefix='/demo')


def register_shell_context(app: Flask):
    from app.models.user import User, Group, Auth
    from app.models.friend_links import FriendLinks
    from app.models.book import Book
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, FriendLinks=FriendLinks, Group=Group, Auth=Auth, Book=Book)


def register_errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return common_render('page/error/index.html', msg='页面不存在！', code=e.code, url=redirect_back_url()), 404

    @app.errorhandler(Exception)
    def handler(e):
        if isinstance(e, WebException):
            return common_render('page/error/index.html', msg=e.msg, code=e.code, url=redirect_back_url()), e.code
        if isinstance(e, APIException):
            return e
        if isinstance(e, HTTPException):
            e.code = e.code
            e.msg = e.description
            return common_render('page/error/index.html', msg=e.msg, code=e.code, url=redirect_back_url()), e.code
            # error_code = 20000
            # return APIException(msg, code, error_code)
        else:
            if not app.config['DEBUG']:
                import traceback
                app.logger.error(traceback.format_exc())
                return UnknownException()
            else:
                raise e


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def admin():
        click.echo('正在创建管理员账户...')
        admin_account = User.query.filter_by(username='admin').first()
        if admin_account is not None:
            click.echo('管理员账户已存在...正在更新帐号密码为admin...')
            admin_account.username = 'admin'
            admin_account.set_password('admin')
            admin_account.set_admin()
        else:
            admin_account = User(username='admin')
            admin_account.set_password('admin')
            admin_account.set_admin()
            db.session.add(admin_account)
        db.session.commit()
        click.echo('创建成功.')
