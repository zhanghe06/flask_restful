#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: sale_delivery_items.py
@time: 2018-07-24 16:47
"""


from libs.mysql_orm_op import DbInstance
from web_api.databases.yonyou import db
from web_api.models.yonyou import SASaleDeliveryB

db_instance = DbInstance(db)


def get_sale_delivery_items_row_by_id(sale_delivery_items_id):
    """
    通过 id 获取信息
    :param sale_delivery_items_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(SASaleDeliveryB, sale_delivery_items_id)


def get_sale_delivery_items_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(SASaleDeliveryB, *args, **kwargs)


def get_sale_delivery_items_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(SASaleDeliveryB, *args, **kwargs)


def get_sale_delivery_items_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(SASaleDeliveryB, last_pk, limit_num, *args, **kwargs)


def add_sale_delivery_items(sale_delivery_items_data):
    """
    添加信息
    :param sale_delivery_items_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(SASaleDeliveryB, sale_delivery_items_data)


def edit_sale_delivery_items(sale_delivery_items_id, sale_delivery_items_data):
    """
    修改信息
    :param sale_delivery_items_id:
    :param sale_delivery_items_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(SASaleDeliveryB, sale_delivery_items_id, sale_delivery_items_data)


def delete_sale_delivery_items(sale_delivery_items_id):
    """
    删除信息
    :param sale_delivery_items_id:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.delete(SASaleDeliveryB, sale_delivery_items_id)


def get_sale_delivery_items_pagination(page=1, per_page=10, *args, **kwargs):
    """
    获取列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = db_instance.get_pagination(SASaleDeliveryB, page, per_page, *args, **kwargs)
    return rows


def delete_sale_delivery_items_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(SASaleDeliveryB)


def count_sale_delivery_items(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(SASaleDeliveryB, *args, **kwargs)
