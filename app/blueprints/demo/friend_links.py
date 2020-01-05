# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from app.libs.redprints import Redprint
from app.libs.utils import common_render
from app.models.friend_links import FriendLinks
from app.exceptions.base import Success, NotFound
from app.extensions import db
from flask import request, flash

friend_links_rp = Redprint('friend-links')


@friend_links_rp.route('/list')
def links_list():
    links = FriendLinks.query.all()
    return common_render('page/links/list/index.html', links=links)


@friend_links_rp.route('/add', methods=['GET', 'POST'])
def links_add():
    if request.method == 'POST':
        req = request.form.to_dict()
        f = FriendLinks(title=req['title'], url=req['url'], email=req['email'], create_time=req['create-time'])
        db.session.add(f)
        db.session.commit()
        flash('添加成功！')
    return common_render('page/links/create/index.html')


@friend_links_rp.route('/delete', methods=['POST'])
def delete():
    links = request.json['links']
    for link_id in links:
        link = FriendLinks.query.get(link_id)
        if link is None:
            db.session.rollback()
            raise NotFound(msg='没有找到相关链接')
        db.session.delete(link)
    db.session.commit()
    return Success(msg='删除成功！')
