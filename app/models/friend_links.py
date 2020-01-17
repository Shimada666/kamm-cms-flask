# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from app.extensions import db

class FriendLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    url = db.Column(db.String(100))
    email = db.Column(db.String(40))
    create_time = db.Column(db.String(10))
    show_address = db.Column(db.Boolean, default=False)  # 1首页 0子页