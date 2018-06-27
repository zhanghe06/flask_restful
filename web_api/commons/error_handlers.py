#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: error_handlers.py
@time: 2018-06-27 20:11
"""


from flask import jsonify, make_response
from web_api import app
from web_api.commons.exceptions import errors


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(errors['NotFound']), 404)
