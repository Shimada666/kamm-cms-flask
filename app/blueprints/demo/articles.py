from app.libs.redprints import Redprint
from app.libs.utils import common_render
from app.exceptions.base import Success
from flask import jsonify, request

articles_rp = Redprint('articles')


@articles_rp.route('/list')
def get_list():
    return common_render('page/articles/list/index.html')


@articles_rp.route('/add')
def add_article():
    return common_render('page/articles/add/index.html')


