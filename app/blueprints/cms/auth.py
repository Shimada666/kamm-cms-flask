# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from app.libs.redprints import Redprint
from app.libs.utils import redirect_back_url, common_render, get_ep_infos, find_auth_module
from app.libs.decorators import admin_required
from app.validtors.forms import RegisterForm, NewGroup
from app.extensions import db
from app.models.user import User, Group, Auth
from app.exceptions.base import NotFound, Success
from flask import request, flash, redirect, url_for

auth_rp = Redprint('auth')


@auth_rp.route('/user/create', methods=['GET', 'POST'])
@admin_required
def create_user():
    groups = Group.query.all()
    if request.method == 'POST':
        form = RegisterForm()
        if form.validate_on_submit():
            exists = User.query.filter_by(username=form.username.data).first()
            if exists:
                flash('该用户已被使用，请输入其他的用户名！', 2)
                return common_render('page/manage_user/create/index.html')
            new_user = User(username=form.username.data, email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('添加成功!', 1)
        else:
            flash(form.errors_info)
    return common_render('page/manage_user/create/index.html', groups=groups)


@auth_rp.route('/users')
def get_users():
    ep_infos = get_ep_infos()
    groups = Group.query.all()
    group_id = request.args.get('group_id')
    users = User.query.filter_by(group_id=group_id).all() if group_id else User.query.all()
    return common_render('page/manage_user/list/index.html', users=users, groups=groups, ep_infos=ep_infos)


@auth_rp.route('/user/delete', methods=['POST'])
def delete_user():
    users = request.json['items']
    for user_id in users:
        user = User.query.get(user_id)
        if user is None:
            db.session.rollback()
            raise NotFound(msg='没有找到相关用户')
        db.session.delete(user)
    db.session.commit()
    return Success(msg='删除成功')


@auth_rp.route('/group/create', methods=['GET', 'POST'])
@admin_required
def create_group():
    ep_infos = get_ep_infos()
    if request.method == 'POST':
        form = NewGroup()
        if form.validate_on_submit():
            exists = Group.query.filter_by(name=form.name.data).first()
            if exists:
                flash('分组已存在，不可创建同名分组', 2)
                return common_render('page/manage_group/create/index.html', ep_infos=ep_infos)
            with db.auto_commit():
                group = Group(name=form.name.data, info=form.info.data)
                db.session.add(group)
                db.session.flush()
                for auth in form.auths.data:
                    meta = find_auth_module(auth)
                    if meta:
                        auth = Auth(auth=meta.auth, module=meta.module, group_id=group.id)
                        db.session.add(auth)
            flash('创建成功', 1)
        else:
            flash(form.errors_info)
    return common_render('page/manage_group/create/index.html', ep_infos=ep_infos)


@auth_rp.route('/group/update', methods=['POST'])
@admin_required
def update_group():
    form = NewGroup()
    if form.validate_on_submit():
        with db.auto_commit():
            group = Group.query.filter_by(name=form.name.data).first()
            pre_auths = Auth.query.filter_by(group_id=group.id).all()
            for item in pre_auths:
                db.session.delete(item)
            db.session.flush()
            for auth in form.auths.data:
                meta = find_auth_module(auth)
                if meta:
                    auth = Auth(auth=meta.auth, module=meta.module, group_id=group.id)
                    db.session.add(auth)
        flash('更新成功', 1)
    else:
        flash(form.errors_info)
    return redirect(url_for('cms.auth+get_groups'))


@auth_rp.route('/groups')
def get_groups():
    ep_infos = get_ep_infos()
    groups = Group.query.all()
    return common_render('page/manage_group/list/index.html', groups=groups, ep_infos=ep_infos)


@auth_rp.route('/group/delete', methods=['POST'])
def delete_group():
    groups = request.json['items']
    for group_id in groups:
        group = Group.query.get(group_id)
        if group is None:
            db.session.rollback()
            raise NotFound(msg='没有找到相关用户')
        db.session.delete(group)
    db.session.commit()
    return Success(msg='删除成功')
