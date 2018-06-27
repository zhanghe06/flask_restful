#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test.py
@time: 2018-07-03 17:54
"""

from __future__ import unicode_literals

import time

from web_api.databases.bearings import db
from web_api.models.bearings import Inventory


def test_get_inventory_qty(inventory_id):
    return db.session.query(Inventory).get(inventory_id).stock_qty


def test_update_inventory_qty(inventory_id, qty=1):
    inventory_obj = db.session.query(Inventory).filter(Inventory.id == inventory_id)
    data = {
        'stock_qty': qty
    }
    result = inventory_obj.update(data)
    db.session.commit()
    return result


def test_decrease_inventory(inventory_id, num=1, lock=False):
    inventory_obj = db.session.query(Inventory).filter(Inventory.id == inventory_id)

    time.sleep(2)
    result = False

    # 不加锁
    if not lock:
        if inventory_obj.one().stock_qty >= num:
            time.sleep(2)
            data = {
                'stock_qty': Inventory.stock_qty - num
            }
            result = inventory_obj.update(data)
            db.session.commit()
    # 排他锁
    else:
        if inventory_obj.with_for_update().one().stock_qty >= num:
            time.sleep(2)
            data = {
                'stock_qty': Inventory.stock_qty - num
            }
            result = inventory_obj.update(data)
            db.session.commit()
    return result

