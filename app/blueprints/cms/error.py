# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
from app.libs.redprints import Redprint
from app.libs.utils import common_render

error_rp = Redprint('error')


@error_rp.route('/404')
def not_found():
    return common_render('page/error/404/index.html')
