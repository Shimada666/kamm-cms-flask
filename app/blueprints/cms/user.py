from app.libs.redprints import Redprint
from app.libs.utils import redirect_back, common_render
from app.validtors.forms import LoginForm, ResetPasswordForm, UserInfoForm
from app.models.user import User
from app.extensions import db
from app.exceptions.base import AuthFailed, Success
from flask import request, render_template, redirect, url_for, flash, jsonify, get_flashed_messages
from flask_login import current_user, login_user, logout_user, login_required

user_rp = Redprint('user')


@user_rp.route('/register', methods=['GET', 'POST'])
def register():
    # TODO..
    pass


@user_rp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('已登录！')
        return redirect(url_for('home.index'))
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data.lower()).first()
            if user is not None and user.validate_password(form.password.data):
                flash('登录成功!', 1)
                login_user(user, True)
                return redirect(url_for('home.index'))
            else:
                flash('用户名或密码错误!', 2)
        else:
            flash(form.errors_info)
    return common_render('page/login/index.html')


@user_rp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('已退出！', 1)
    return redirect(url_for('home.index'))


@user_rp.route('/information', methods=['GET', 'POST'])
@login_required
def information():
    if request.method == 'POST':
        form = UserInfoForm()
        if form.validate_on_submit():
            current_user.real_name = form.real_name.data
            current_user.gender = form.gender.data
            current_user.phone = form.phone.data
            current_user.birthday = form.birthday.data
            current_user.email = form.email.data
            current_user.about = form.about.data
            db.session.commit()
            flash('修改成功!', 1)
        else:
            flash(form.errors_info)
    return common_render('page/user/information/index.html')


@user_rp.route('/change_user_info', methods=['POST'])
@login_required
def change_user_info():
    req_body = request.form.to_dict()
    current_user.real_name = req_body['real_name']
    db.session.commit()
    return Success(msg='修改成功!')


@user_rp.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    if request.method == 'POST':
        form = ResetPasswordForm()
        if form.validate_on_submit():
            if current_user.validate_password(form.oldPassword.data):
                current_user.password = form.newPassword.data
                db.session.commit()
                flash('修改成功!', 1)
        else:
            flash(form.errors_info)
    return common_render('page/user/reset_password/index.html')
