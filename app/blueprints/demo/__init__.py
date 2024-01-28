from flask import Blueprint
from app.libs.utils import common_render


def create_demo():
    demo = Blueprint('demo', __name__)

    from .friend_links import friend_links_rp
    from .book import book_rp
    friend_links_rp.register(demo)
    book_rp.register(demo)

    return demo


demo_bp = create_demo()


@demo_bp.route('/main')
def main_page():
    return common_render('page/main/index.html')
