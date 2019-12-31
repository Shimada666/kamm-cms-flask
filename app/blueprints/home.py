# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint, render_template
from app.libs.utils import common_render
from app.libs.decorators import admin_required


def create_home():
    home = Blueprint('home', __name__)
    return home


home_bp = create_home()


@home_bp.route('/')
def index():
    return common_render('page/index/index.html')


@home_bp.route('/404')
# @admin_required
def not_found():
    # return common_render('page/error/404/index.html')
    return common_render('page/error/index.html', msg='qwe', code=123)
