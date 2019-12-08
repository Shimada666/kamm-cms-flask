# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

login_manager = LoginManager()
db = SQLAlchemy()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'cms.user+login'
