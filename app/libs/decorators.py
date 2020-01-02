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
from app.exceptions.base import WebAuthFailed


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            raise WebAuthFailed(msg='只有超级管理员可操作')
        return fn(*args, **kwargs)

    return wrapper


def group_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # not admin
        if not current_user.is_authenticated:
            raise WebAuthFailed(msg='您还未登录！')
        if not current_user.is_admin:
            group_id = current_user.group_id
            if group_id is None:
                raise WebAuthFailed(msg='您还不属于任何权限组，请联系超级管理员获得权限')
            from .utils import is_user_allowed
            it = is_user_allowed(group_id)
            if not it:
                raise WebAuthFailed(msg='权限不够，请联系超级管理员获得权限')
            else:
                return fn(*args, **kwargs)
        else:
            return fn(*args, **kwargs)

    return wrapper
