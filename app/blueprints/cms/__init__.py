"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import Blueprint


def create_cms():
    cms = Blueprint('cms', __name__)
    # from .admin import admin_api
    from .user import user_rp
    from .system import system_rp
    from .error import error_rp
    # from .log import log_api
    # from .file import file_api
    # from .test import test_api
    # admin_api.register(cms)
    user_rp.register(cms)
    system_rp.register(cms)
    error_rp.register(cms)
    # log_api.register(cms)
    # file_api.register(cms)
    # test_api.register(cms)
    return cms


cms_bp = create_cms()

