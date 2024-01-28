from flask import Blueprint, render_template
from app.libs.utils import common_render
from app.libs.decorators import admin_required, group_required
from app.libs.utils import route_meta, route_meta_infos


def create_home():
    home = Blueprint('home', __name__)
    return home


home_bp = create_home()


@home_bp.route('/')
def index():
    return common_render('page/index/index.html')


@home_bp.route('/404')
@group_required
def not_found():
    return common_render('page/error/index.html', msg='测试', code=123)
