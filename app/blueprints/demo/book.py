from app.libs.decorators import group_required
from app.libs.redprints import Redprint
from app.libs.utils import common_render, route_meta
from app.models.book import Book
from app.exceptions.base import Success, NotFound
from app.extensions import db
from flask import request, flash

book_rp = Redprint('book')


@book_rp.route('/list')
@route_meta(auth='图书列表', module='图书')
@group_required
def links_list():
    links = Book.query.all()
    return common_render('page/book/list/index.html', links=links)


@book_rp.route('/add', methods=['GET', 'POST'])
@route_meta(auth='添加图书', module='图书')
@group_required
def links_add():
    if request.method == 'POST':
        req = request.form.to_dict()
        f = Book(title=req['title'], url=req['url'], description=req['description'], author=req['author'],
                 create_time=req['create-time'])
        db.session.add(f)
        db.session.commit()
        flash('添加成功！')
    return common_render('page/book/create/index.html')


@book_rp.route('/delete', methods=['POST'])
@route_meta(auth='删除图书', module='图书')
@group_required
def delete():
    links = request.json['items']
    for link_id in links:
        link = Book.query.get(link_id)
        if link is None:
            db.session.rollback()
            raise NotFound(msg='没有找到相关链接')
        db.session.delete(link)
    db.session.commit()
    return Success(msg='删除成功！')
