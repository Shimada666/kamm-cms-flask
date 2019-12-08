# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin
from uuid import uuid4
from flask import request, redirect, url_for, render_template
import os


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path, debug=True):
        if debug:
            ver = "%s" % uuid4()
        else:
            ver = "%s" % (22222222)
        path = "/static" + path + "?ver=" + ver
        return UrlManager.build_url(path)