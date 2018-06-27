#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_high_concurrency.py
@time: 2018-07-03 14:14
"""

from __future__ import print_function
from __future__ import unicode_literals

import unittest
import grequests
from requests.auth import HTTPBasicAuth

from web_api.bearings.apis.test import (
    test_get_inventory_qty,
    test_update_inventory_qty,
)


class HighConcurrencyTest(unittest.TestCase):
    """
    高并发测试
    """

    def setUp(self):
        self.auth_username = 'username'
        self.auth_password = 'password'
        self.base_auth = HTTPBasicAuth(self.auth_username, self.auth_password)

        self.url_with_lock = 'http://0.0.0.0:5000/bearings/test_decrease_inventory/1?num=100&lock=true'
        self.url_without_lock = 'http://0.0.0.0:5000/bearings/test_decrease_inventory/1?num=100&lock=false'

        self.inventory_id = 1
        self.qty_init = 100

        # 准备初始数据
        self.qty = test_get_inventory_qty(self.inventory_id)
        test_update_inventory_qty(self.inventory_id, self.qty_init)

    def test_without_for_update(self):
        """
        测试不加锁
        :return:
        """
        urls = [self.url_without_lock] * 2
        rs = [grequests.post(u, auth=self.base_auth) for u in urls]
        grequests.map(rs)

        self.assertEqual(rs[0].response.status_code, 202)
        self.assertEqual(rs[1].response.status_code, 202)

        qty = test_get_inventory_qty(self.inventory_id)
        self.assertEqual(qty, -100)

    def test_with_for_update(self):
        """
        测试排他锁
        :return:
        """
        urls = [self.url_with_lock] * 2
        rs = [grequests.post(u, auth=self.base_auth) for u in urls]
        grequests.map(rs)

        status_code_set = set([rs_item.response.status_code for rs_item in rs])

        # 此处不确定执行顺序, 所以用集合断言
        self.assertEqual(status_code_set, {202, 400})

        qty = test_get_inventory_qty(self.inventory_id)
        self.assertEqual(qty, 0)

    def tearDown(self):
        # 还原原始数据
        test_update_inventory_qty(1, self.qty)


if __name__ == '__main__':
    unittest.main()
