from app.extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    url = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    author = db.Column(db.String(1000))
    create_time = db.Column(db.String(10))
