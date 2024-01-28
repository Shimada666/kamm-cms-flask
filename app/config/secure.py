# 安全性配置
from app.config.setting import BaseConfig
import sys
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class DevelopmentSecure(BaseConfig):
    """
    开发环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('db_url', 'sqlite:///../kamm.db')
    # SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'


class ProductionSecure(BaseConfig):
    """
    生产环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('db_url', 'mysql+cymysql://root:root@localhost/kamm?charset=utf8mb4')
    # SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'
