from app.libs.redprints import Redprint
from app.libs.utils import redirect_back_url, common_render
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
        },
        {
            "title": "图书管理",
            "icon": "&#xe64c;",
            "href": f"",
            "spread": False,
            "children": [
                {
                    "title": "图书列表",
                    "href": f"{url_for('demo.book+links_list')}",
                    "spread": False
                },
                {
                    "title": "添加图书",
                    "href": f"{url_for('demo.book+links_add')}",
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
    if current_user.is_authenticated and current_user.is_admin:
        admin_navs = [
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
                        "href": f"{url_for('cms.auth+get_groups')}",
                        "spread": False
                    },
                    {
                        "title": "添加分组",
                        "href": f"{url_for('cms.auth+create_group')}",
                        "spread": False,
                    }
                ]
            },
        ]
        for nav in admin_navs:
            res.append(nav)
    return jsonify(res)


@system_rp.route('/info')
def info():
    role = "管理员" if current_user.is_admin else "用户"
    res = {
        "框架名称": "图书管理系统v1",
        "框架版本": "v1",
        "主页位置": "/",
        "服务器版本": f"{platform.platform()}",
        "数据库版本": "sqlite3",
        "上传限制": "2M",
        "用户角色": role,
        "框架描述": "一套flask开发的简单图书管理系统，包含权限管理",
    }
    return common_render('page/system_info/index.html', info=res)
