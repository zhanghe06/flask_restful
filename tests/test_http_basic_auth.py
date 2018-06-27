#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_http_basic_auth.py
@time: 2018-06-21 11:17
"""


from __future__ import print_function
from __future__ import unicode_literals

import unittest
import requests
from requests.auth import HTTPBasicAuth


class HttpBasicAuthTest(unittest.TestCase):
    """
    认证测试
    """

    def setUp(self):
        self.auth_username = 'username'
        self.auth_password = 'password'
        self.auth_url = 'http://0.0.0.0:5000/token'
        self.session = requests.session()

    def test_auth_success(self):
        """
        测试认证成功
        :return:
        """
        base_auth = HTTPBasicAuth(self.auth_username, self.auth_password)
        res = self.session.get(self.auth_url, auth=base_auth)
        self.assertEqual(res.status_code, 200)

    def test_auth_failure(self):
        """
        测试认证失败
        :return:
        """
        res = self.session.get(self.auth_url)
        self.assertEqual(res.status_code, 401)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
