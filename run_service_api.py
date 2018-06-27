#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_service_api.py
@time: 2018-05-30 20:04
"""


from web_api import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
