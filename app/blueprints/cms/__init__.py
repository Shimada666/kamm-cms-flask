from flask import Blueprint


def create_cms():
    cms = Blueprint('cms', __name__)
    # from .admin import admin_api
    from .user import user_rp
    from .system import system_rp
    from .auth import auth_rp
    # from .log import log_api
    # from .file import file_api
    # from .test import test_api
    # admin_api.register(cms)
    user_rp.register(cms)
    system_rp.register(cms)
    auth_rp.register(cms)
    # log_api.register(cms)
    # file_api.register(cms)
    # test_api.register(cms)
    return cms


cms_bp = create_cms()

