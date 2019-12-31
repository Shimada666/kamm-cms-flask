# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from functools import wraps

from flask import request, abort
from flask_login import current_user
from app.exceptions.base import AuthFailed, WebException


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            raise WebException(code=403, msg='只有超级管理员可操作')
        return fn(*args, **kwargs)

    return wrapper

# def group_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         # check current user is active or not
#         # 判断当前用户是否为激活状态
#         # not admin
#         if not current_user.is_admin:
#             group_id = current_user.group_id
#             if group_id is None:
#                 raise AuthFailed(msg='您还不属于任何权限组，请联系超级管理员获得权限')
#             from .core import is_user_allowed
#             it = is_user_allowed(group_id)
#             if not it:
#                 raise AuthFailed(msg='权限不够，请联系超级管理员获得权限')
#             else:
#                 return fn(*args, **kwargs)
#         else:
#             return fn(*args, **kwargs)
#
#     return wrapper


# def login_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         _check_is_active(current_user=get_current_user())
#         return fn(*args, **kwargs)
#
#     return wrapper
