
links = [
    {
        "linksId": "1",
        "linksName": "layui - 经典模块化前端框架",
        "linksUrl": "http://www.layui.com",
        "masterEmail": "xianxin@layui.com",
        "linksTime": "2017-05-14",
        "showAddress": "首页"
    }, {
        "linksId": "2",
        "linksName": "layer官方演示与讲解",
        "linksUrl": "http://layer.layui.com",
        "masterEmail": "xianxin@layer.com",
        "linksTime": "2017-05-15",
        "showAddress": "子页"
    }, {
        "linksId": "3",
        "linksName": "layui - 前端框架官方社区",
        "linksUrl": "http://fly.layui.com",
        "masterEmail": "xianxin@fly.com",
        "linksTime": "2017-05-12",
        "showAddress": "子页"
    }]

from app import create_app
from app.extensions import db
from app.models.friend_links import FriendLinks


def main():
    app = create_app()
    with app.app_context():
        with db.auto_commit():
            for link in links:
                address = True if link['showAddress'] == '首页' else False
                l = FriendLinks(id=link['linksId'], title=link['linksName'], url=link['linksUrl'],
                                email=link['masterEmail'], create_time=link['linksTime'], show_address=address)
                db.session.add(l)


if __name__ == '__main__':
    main()
