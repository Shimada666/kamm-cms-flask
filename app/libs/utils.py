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
from app.models.user import Auth
import os
from collections import namedtuple


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def redirect_back(default='home.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


# 统一渲染方法
def common_render(template, **context):
    context['path'] = template
    return render_template(template, **context)


# 路由函数的权限和模块信息(meta信息)
Meta = namedtuple('meta', ['auth', 'module'])

#       -> endpoint -> func
# auth                      -> module
#       -> endpoint -> func

# 记录路由函数的权限和模块信息
route_meta_infos = {}
ep_meta = {}


def route_meta(auth, module='common', mount=True):
    """
    记录路由函数的信息
    记录路由函数访问的推送信息模板
    注：只有使用了 route_meta 装饰器的函数才会被记录到权限管理的map中
    :param auth: 权限
    :param module: 所属模块
    :param mount: 是否挂在到权限中（一些视图函数需要说明，或暂时决定不挂在到权限中，则设置为False）
    :return:
    """

    def wrapper(func):
        if mount:
            name = func.__name__ + str(func.__hash__())
            existed = route_meta_infos.get(name, None) and route_meta_infos.get(name).module == module
            if existed:
                raise Exception("func's name cant't be repeat in a same module")
            else:
                route_meta_infos.setdefault(name, Meta(auth, module))
        return func

    return wrapper


def verity_user_in_group(group_id, auth, module):
    return Auth.query.filter_by(group_id=group_id, auth=auth, module=module).first()


def is_user_allowed(group_id):
    """查看当前user有无权限访问该路由函数"""
    ep = request.endpoint
    # 根据 endpoint 查找 authority
    meta = ep_meta.get(ep)
    return verity_user_in_group(group_id, meta.auth, meta.module)


def find_auth_module(auth):
    """ 通过权限寻找meta信息"""
    for _, meta in ep_meta.items():
        if meta.auth == auth:
            return meta
    return None


def get_ep_infos():
    """ 返回权限管理中的所有视图函数的信息，包含它所属module """
    infos = {}
    for ep, meta in ep_meta.items():
        mod = infos.get(meta.module, None)
        if mod:
            sub = mod.get(meta.auth, None)
            if sub:
                sub.append(ep)
            else:
                mod[meta.auth] = [ep]
        else:
            infos.setdefault(meta.module, {meta.auth: [ep]})

    return infos
