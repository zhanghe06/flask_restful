#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2018-07-24 00:14
"""

from web_api.yonyou import yonyou_api
from web_api.yonyou.resources.partner import (
    PartnerResource,
    PartnerListResource,
    PartnerPaginationResource
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
