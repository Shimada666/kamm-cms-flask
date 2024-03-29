from app.extensions import db

class FriendLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    url = db.Column(db.String(100))
    email = db.Column(db.String(40))
    create_time = db.Column(db.String(10))
    show_address = db.Column(db.Boolean, default=False)  # 1首页 0子页