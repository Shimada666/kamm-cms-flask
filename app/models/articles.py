from app.extensions import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    author = db.Column(db.String(20), default='未名')
    status = db.Column(db.Boolean)  # 1通过 0待审核
    look = db.Column(db.Boolean)  # 1能看 0不能看
    show = db.Column(db.Boolean)  # 1展示 0不展示
    create_time = db.Column(db.String(10))
