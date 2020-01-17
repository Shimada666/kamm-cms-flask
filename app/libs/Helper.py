# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2019 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""

import os
import uuid
from flask import current_app


class Helper:
    @classmethod
    def _css_in_template(cls, url: str) -> str:
        if current_app.config['DEBUG']:
            return f'<link rel="stylesheet" href="{url}.css?v={uuid.uuid4()}" />'
        return f'<link rel="stylesheet" href="{url}.css" />'

    @classmethod
    def _less_in_template(cls, url: str) -> str:
        if current_app.config['DEBUG']:
            return f'<link rel="stylesheet/less" type="text/less" href="{url}.less?v={uuid.uuid4()}" />'
        return f'<link rel="stylesheet/less" type="text/less" href="{url}.less" />'

    @classmethod
    def _script_in_template(cls, url: str) -> str:
        if current_app.config['DEBUG']:
            return f'<script type="text/javascript" src="{url}.js?v={uuid.uuid4()}"></script>'
        return f'<script type="text/javascript" src="{url}.js"></script>'

    @classmethod
    def _get_path(cls, entry):
        return '/' + os.path.splitext(entry)[0]

    @classmethod
    def get_script(cls, entry: str = ''):
        path = cls._get_path(entry)
        return cls._script_in_template(f'{path}')

    @classmethod
    def get_style(cls, entry: str = ''):
        path = cls._get_path(entry)
        prefix_file_name = path.rsplit('/', 1)[-1]
        relative_dir_path = path.rsplit('/', 1)[0][1:]
        static_path = current_app.static_folder
        target_path = os.path.join(static_path, relative_dir_path)
        file_list = os.listdir(target_path)
        if f'{prefix_file_name}.less' in file_list:
            return cls._less_in_template(f'{path}')
        else:
            return cls._css_in_template(f'{path}')
