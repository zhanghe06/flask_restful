#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_http_token_auth.py
@time: 2018-06-21 11:17
"""


from __future__ import print_function
from __future__ import unicode_literals

import unittest
import requests
from requests.auth import HTTPBasicAuth, AuthBase


class HTTPTokenAuth(AuthBase):
    """Attaches HTTP Token Authentication to the given Request object."""

    def __init__(self, token, scheme='Bearer'):
        self.scheme = scheme
        self.token = token

    def __eq__(self, other):
        return all([
            self.token == getattr(other, 'token', None),
        ])

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers['Authorization'] = '%s %s' % (self.scheme, self.token)
        return r


class HttpTokenAuthTest(unittest.TestCase):
    """
    认证测试
    """

    def setUp(self):
        self.scheme = 'Bearer'
        self.auth_username = 'username'
        self.auth_password = 'password'
        self.auth_url = 'http://0.0.0.0:5000/token'
        self.news_url = 'http://0.0.0.0:5000/news/fetch_results?last_pk=1000&limit_num=2'
        self.session = requests.session()
        self._get_token()

    def _get_token(self):
        base_auth = HTTPBasicAuth(self.auth_username, self.auth_password)
        res = self.session.get(self.auth_url, auth=base_auth)
        self.token = res.json()['token']

    def test_auth_success_request_headers(self):
        """
        测试认证成功 - header方式
        :return:
        """
        request_headers = {
            'Authorization': '%s %s' % (self.scheme, self.token),
        }
        res = self.session.get(self.news_url, headers=request_headers)
        self.assertEqual(res.status_code, 200)

    def test_auth_failure_request_headers(self):
        """
        测试认证失败 - header方式
        :return:
        """
        request_headers = {
            'Authorization': '%s %s' % (self.scheme, 'error_token'),
        }
        res = self.session.get(self.news_url, headers=request_headers)
        self.assertEqual(res.status_code, 403)

    def test_auth_success_token_auth(self):
        """
        测试认证成功 - auth方式
        :return:
        """
        token_auth = HTTPTokenAuth(self.token)
        res = self.session.get(self.news_url, auth=token_auth)
        self.assertEqual(res.status_code, 200)

    def test_auth_failure_token_auth(self):
        """
        测试认证失败 - auth方式
        :return:
        """
        token_auth = HTTPTokenAuth('error_token')
        res = self.session.get(self.news_url, auth=token_auth)
        self.assertEqual(res.status_code, 403)

    def test_auth_failure_empty(self):
        """
        测试认证失败 - 空值
        :return:
        """
        res = self.session.get(self.news_url)
        self.assertEqual(res.status_code, 403)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
