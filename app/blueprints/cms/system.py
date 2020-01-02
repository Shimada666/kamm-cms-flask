# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

from app.libs.redprints import Redprint
from app.libs.utils import redirect_back, common_render
from app.validtors.forms import LoginForm, ResetPasswordForm
from app.models.user import User
from app.extensions import db
from app.exceptions.base import AuthFailed, Success
from flask import request, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user, login_required
import os
import platform

system_rp = Redprint('system')


@system_rp.route('/navs')
def navs():
    if current_user.is_authenticated and current_user.is_admin:
        res = [
            {
                "title": "后台首页",
                "icon": "icon-computer",
                "href": f"{url_for('demo.main_page')}",
                "spread": False
            },
            {
                "title": "用户管理",
                "icon": "&#xe612;",
                "spread": False,
                "children": [
                    {
                        "title": "用户列表",
                        "href": f"{url_for('cms.auth+get_users')}",
                        "spread": False
                    },
                    {
                        "title": "添加用户",
                        "href": f"{url_for('cms.auth+create_user')}",
                        "spread": False,
                    }
                ]
            },
            {
                "title": "分组管理",
                "icon": "&#xe647;",
                "spread": False,
                "children": [
                    {
                        "title": "分组列表",
                        "href": f"{url_for('demo.friend-links+links_list')}",
                        "spread": False
                    },
                    {
                        "title": "添加分组",
                        "href": f"{url_for('demo.friend-links+links_add')}",
                        "spread": False,
                    }
                ]
            },
            {
                "title": "友情链接",
                "icon": "&#xe64c;",
                "href": f"",
                "spread": False,
                "children": [
                    {
                        "title": "链接列表",
                        "href": f"{url_for('demo.friend-links+links_list')}",
                        "spread": False
                    },
                    {
                        "title": "添加链接",
                        "href": f"{url_for('demo.friend-links+links_add')}",
                        "spread": False,
                    }
                ]
            }, {
                "title": "系统基本参数",
                "icon": "&#xe631;",
                "href": f"{url_for('cms.system+info')}",
                "spread": False
            },
        ]
    else:
        res = [
            {
                "title": "后台首页",
                "icon": "icon-computer",
                "href": f"{url_for('demo.main_page')}",
                "spread": False
            },
            {
                "title": "友情链接",
                "icon": "&#xe64c;",
                "href": f"",
                "spread": False,
                "children": [
                    {
                        "title": "链接列表",
                        "href": f"{url_for('demo.friend-links+links_list')}",
                        "spread": False
                    },
                    {
                        "title": "添加链接",
                        "href": f"{url_for('demo.friend-links+links_add')}",
                        "spread": False,
                    }
                ]
            }, {
                "title": "系统基本参数",
                "icon": "&#xe631;",
                "href": f"{url_for('cms.system+info')}",
                "spread": False
            },
        ]
    return jsonify(res)


@system_rp.route('/info')
def info():
    res = {
        "框架名称": "kamm后台管理框架",
        "框架版本": "v0.0.1",
        "作者": "Shimada666",
        "主页位置": "/",
        "服务器版本": f"{platform.platform()}",
        "数据库版本": "mysql5.7",
        "上传限制": "2M",
        "用户角色": "总管理员",
        "框架描述": "一套flask+layui的开发框架",
        "技术支持": "copyright @2019 Shimada666",
    }
    return common_render('page/system_info/index.html', info=res)
