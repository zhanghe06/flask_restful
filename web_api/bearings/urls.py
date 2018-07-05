#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2018-06-28 00:48
"""


from web_api.bearings import bearings_api
from web_api.bearings.resources.inventory import (
    InventoryResource,
    InventoryListResource,
    InventoryPaginationResource,
)

from web_api.bearings.resources.customer import (
    CustomerResource,
    CustomerListResource,
    CustomerPaginationResource,
)

from web_api.bearings.resources.test import (
    TestDecreaseInventoryResource
)


# 库存
bearings_api.add_resource(
    InventoryResource,
    '/inventory/<int:pk>',
    endpoint='inventory',
    strict_slashes=False
)

bearings_api.add_resource(
    InventoryListResource,
    '/inventories',
    endpoint='inventories',
    strict_slashes=False
)

bearings_api.add_resource(
    InventoryPaginationResource,
    '/inventories/pagination',
    endpoint='inventories_pagination',
    strict_slashes=False
)

bearings_api.add_resource(
    TestDecreaseInventoryResource,
    '/test_decrease_inventory/<int:pk>',
    endpoint='test_decrease_inventory',
    strict_slashes=False
)


# 客户
bearings_api.add_resource(
    CustomerResource,
    '/customer/<int:pk>',
    endpoint='customer',
    strict_slashes=False
)

bearings_api.add_resource(
    CustomerListResource,
    '/customers',
    endpoint='customers',
    strict_slashes=False
)

bearings_api.add_resource(
    CustomerPaginationResource,
    '/customers/pagination',
    endpoint='customers_pagination',
    strict_slashes=False
)
