#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2018-07-24 00:14
"""

from web_api.yonyou import yonyou_api
from web_api.yonyou.resources.current_stock import (
    CurrentStockResource,
    CurrentStockListResource,
    CurrentStockPaginationResource
)
from web_api.yonyou.resources.enum import (
    EnumResource,
    EnumListResource,
    EnumPaginationResource
)
from web_api.yonyou.resources.enum_items import (
    EnumItemsResource,
    EnumItemsListResource,
    EnumItemsPaginationResource
)
from web_api.yonyou.resources.inventory import (
    InventoryResource,
    InventoryListResource,
    InventoryPaginationResource,
    InventoryListSyncResource,
)
from web_api.yonyou.resources.partner import (
    PartnerResource,
    PartnerListResource,
    PartnerPaginationResource,
    PartnerListSyncResource,
)
from web_api.yonyou.resources.sale_delivery import (
    SaleDeliveryResource,
    SaleDeliveryListResource,
    SaleDeliveryPaginationResource
)
from web_api.yonyou.resources.sale_invoice import (
    SaleInvoiceResource,
    SaleInvoiceListResource,
    SaleInvoicePaginationResource
)
from web_api.yonyou.resources.sale_order import (
    SaleOrderResource,
    SaleOrderListResource,
    SaleOrderPaginationResource
)


# 当前库存
yonyou_api.add_resource(
    CurrentStockResource,
    '/current_stock/<int:pk>',
    endpoint='current_stock',
    strict_slashes=False
)

yonyou_api.add_resource(
    CurrentStockListResource,
    '/current_stocks',
    endpoint='current_stocks',
    strict_slashes=False
)

yonyou_api.add_resource(
    CurrentStockPaginationResource,
    '/current_stocks/pagination',
    endpoint='current_stocks_pagination',
    strict_slashes=False
)


# 枚举类型
yonyou_api.add_resource(
    EnumResource,
    '/enum/<int:pk>',
    endpoint='enum',
    strict_slashes=False
)

yonyou_api.add_resource(
    EnumListResource,
    '/enums',
    endpoint='enums',
    strict_slashes=False
)

yonyou_api.add_resource(
    EnumPaginationResource,
    '/enums/pagination',
    endpoint='enums_pagination',
    strict_slashes=False
)


# 枚举类型明细
yonyou_api.add_resource(
    EnumItemsResource,
    '/enum_item/<int:pk>',
    endpoint='enum_item',
    strict_slashes=False
)

yonyou_api.add_resource(
    EnumItemsListResource,
    '/enum_items',
    endpoint='enum_items',
    strict_slashes=False
)

yonyou_api.add_resource(
    EnumItemsPaginationResource,
    '/enum_items/pagination',
    endpoint='enum_items_pagination',
    strict_slashes=False
)


# 产品
yonyou_api.add_resource(
    InventoryResource,
    '/inventory/<int:pk>',
    endpoint='inventory',
    strict_slashes=False
)

yonyou_api.add_resource(
    InventoryListResource,
    '/inventories',
    endpoint='inventories',
    strict_slashes=False
)

yonyou_api.add_resource(
    InventoryPaginationResource,
    '/inventories/pagination',
    endpoint='inventories_pagination',
    strict_slashes=False
)

yonyou_api.add_resource(
    InventoryListSyncResource,
    '/inventories/sync',
    endpoint='inventories_sync',
    strict_slashes=False
)


# 往来单位
yonyou_api.add_resource(
    PartnerResource,
    '/partner/<int:pk>',
    endpoint='partner',
    strict_slashes=False
)

yonyou_api.add_resource(
    PartnerListResource,
    '/partners',
    endpoint='partners',
    strict_slashes=False
)

yonyou_api.add_resource(
    PartnerPaginationResource,
    '/partners/pagination',
    endpoint='partners_pagination',
    strict_slashes=False
)

yonyou_api.add_resource(
    PartnerListSyncResource,
    '/partners/sync',
    endpoint='partners_sync',
    strict_slashes=False
)


# 销售出库
yonyou_api.add_resource(
    SaleDeliveryResource,
    '/sale_delivery/<int:pk>',
    endpoint='sale_delivery',
    strict_slashes=False
)

yonyou_api.add_resource(
    SaleDeliveryListResource,
    '/sale_deliveries',
    endpoint='sale_deliveries',
    strict_slashes=False
)

yonyou_api.add_resource(
    SaleDeliveryPaginationResource,
    '/sale_deliveries/pagination',
    endpoint='sale_deliveries_pagination',
    strict_slashes=False
)


# 销售发票
yonyou_api.add_resource(
    SaleInvoiceResource,
    '/sale_invoice/<int:pk>',
    endpoint='sale_invoice',
    strict_slashes=False
)

yonyou_api.add_resource(
    SaleInvoiceListResource,
    '/sale_invoices',
    endpoint='sale_invoices',
    strict_slashes=False
)

yonyou_api.add_resource(
    SaleInvoicePaginationResource,
    '/sale_invoices/pagination',
    endpoint='sale_invoices_pagination',
    strict_slashes=False
)


# 销售订单
yonyou_api.add_resource(
    SaleOrderResource,
    '/sale_order/<int:pk>',
    endpoint='sale_order',
    strict_slashes=False
)

yonyou_api.add_resource(
    SaleOrderListResource,
    '/sale_orders',
    endpoint='sale_orders',
    strict_slashes=False
)

yonyou_api.add_resource(
    SaleOrderPaginationResource,
    '/sale_orders/pagination',
    endpoint='sale_orders_pagination',
    strict_slashes=False
)
