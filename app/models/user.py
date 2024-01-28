from flask_login import UserMixin
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum


# status for user is admin
# 是否为超级管理员的枚举
class UserAdmin(Enum):
    COMMON = 1
    ADMIN = 2


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # : name of group
    # : 权限组名称
    name = db.Column(db.String(60), comment='权限组名称')
    # a description of a group
    # 权限组描述
    info = db.Column(db.String(255), comment='权限组描述')

    users = db.relationship('User', backref='group')
    auths = db.relationship('Auth', backref='group', cascade='all')


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
    admin = db.Column(db.SmallInteger, nullable=False, default=1,
                      comment='是否为超级管理员 ;  1 -> 普通用户 |  2 -> 超级管理员')

    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    @property
    def is_admin(self):
        return self.admin == UserAdmin.ADMIN.value

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def set_admin(self):
        self.admin = UserAdmin.ADMIN.value

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def reset_password(self, old_password, new_password):
        #: attention,remember to commit
        #: 注意，修改密码后记得提交至数据库
        # if self.validate_password(new_password):
        #     self.set_password(new_password)
        if self.validate_password(old_password):
            self.password = new_password
            return True
        return False


class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # : belongs to which group
    # : 所属权限组id
    # group_id = db.Column(db.Integer, nullable=False, comment='所属权限组id')
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    # : authority field
    # : 权限字段
    auth = db.Column(db.String(60), comment='权限字段')
    # : authority module, default common , which can sort authorities
    # : 权限的模块
    module = db.Column(db.String(50), comment='权限的模块')
