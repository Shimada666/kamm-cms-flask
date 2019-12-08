"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint
from app.libs.utils import common_render


def create_demo():
    demo = Blueprint('demo', __name__)

    from .friend_links import friend_links_rp
    from .articles import articles_rp
    friend_links_rp.register(demo)
    articles_rp.register(demo)

    return demo


demo_bp = create_demo()


@demo_bp.route('/main')
def main_page():
    return common_render('page/main/index.html')

#
# @demo_bp.route('/articles-list')
# def articles_list():
#     return common_render('page/articles/list/index.html')

#
# @demo_bp.route('/friend-links')
# def friend_links():
#     return common_render('page/links/list/index.html')
