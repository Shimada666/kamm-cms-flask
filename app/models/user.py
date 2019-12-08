from flask_login import UserMixin
from app.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(40))
    real_name = db.Column(db.String(10))
    gender = db.Column(db.Enum('男', '女', '保密'))
    phone = db.Column(db.String(15))
    birthday = db.Column(db.String(10))
    home_address = db.Column(db.String(30))
    hobbies = db.Column(db.String(50))
    avatar = db.Column(db.String(64))
    about = db.Column(db.Text)

    def validate_password(self, password):
        if self.password == password:
            return True
        return False
        # return check_password_hash(self.password_hash, password)
