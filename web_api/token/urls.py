#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2018-06-21 16:48
"""


from web_api.token.resources import TokenResource

from web_api.token import token_api


token_api.add_resource(TokenResource, '/', endpoint='token', strict_slashes=False)
