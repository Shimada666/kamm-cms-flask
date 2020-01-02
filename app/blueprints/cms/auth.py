# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from app.libs.redprints import Redprint
from app.libs.utils import redirect_back, common_render
from app.libs.decorators import admin_required
from app.validtors.forms import RegisterForm
from app.extensions import db
from app.models.user import User, Group
from app.exceptions.base import NotFound, Success
from flask import request, flash

auth_rp = Redprint('auth')


@auth_rp.route('/user/add', methods=['GET', 'POST'])
@admin_required
def create_user():
    if request.method == 'POST':
        form = RegisterForm()
        if form.validate_on_submit():
            exists = User.query.filter_by(username=form.username.data).first()
            if exists:
                flash('该用户已被使用，请输入其他的用户名！', 2)
                return common_render('page/manage_user/add/index.html')
            new_user = User(username=form.username.data, email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('添加成功!', 1)
        else:
            flash(form.errors_info)
    return common_render('page/manage_user/create/index.html')


@auth_rp.route('/users')
def get_users():
    groups = Group.query.all()
    group_id = request.args.get('group_id')
    users = User.query.filter_by(group_id=group_id).all() if group_id else User.query.all()
    return common_render('page/manage_user/list/index.html', users=users, groups=groups)


@auth_rp.route('/user/delete', methods=['POST'])
def delete_user():
    users = request.json['users']
    for user_id in users:
        user = User.query.get(user_id)
        if user is None:
            db.session.rollback()
            raise NotFound(msg='没有找到相关用户')
        db.session.delete(user)
    db.session.commit()
    return Success(msg='删除成功')
