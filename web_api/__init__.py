#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2018-05-30 18:59
"""

from flask import Flask

from config import current_config
from web_api.commons.exceptions import errors

from web_api.token.blueprints import token_bp
from web_api.news.blueprints import news_bp
from web_api.bearings.blueprints import bearings_bp
from web_api.yonyou.blueprints import yonyou_bp


app = Flask(__name__)

# Load Config
app.config.from_object(current_config)

# Register Blueprint
app.register_blueprint(token_bp)
app.register_blueprint(news_bp)
app.register_blueprint(bearings_bp)
app.register_blueprint(yonyou_bp)


# Add Resource Urls
# 注意顺序, 避免循环导入
from web_api import urls

from web_api.token import urls
from web_api.news import urls
from web_api.bearings import urls
from web_api.yonyou import urls

# Error Handlers
from web_api.commons import error_handlers
