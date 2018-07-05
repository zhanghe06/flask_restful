#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: customer.py
@time: 2018-07-05 16:57
"""

import datetime

from libs.mysql_orm_op import DbInstance
from web_api.databases.bearings import db
from web_api.models.bearings import Customer

from web_api.bearings.apis.customer_contact import get_customer_contact_rows
from web_api.bearings.apis.customer_invoice import get_customer_invoice_row_by_id


db_instance = DbInstance(db)


def get_customer_row_by_id(customer_id):
    """
    通过 id 获取信息
    :param customer_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(Customer, customer_id)


def get_customer_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(Customer, *args, **kwargs)


def get_customer_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(Customer, *args, **kwargs)


def get_customer_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(Customer, last_pk, limit_num, *args, **kwargs)


def add_customer(customer_data):
    """
    添加信息
    :param customer_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(Customer, customer_data)


def edit_customer(customer_id, customer_data):
    """
    修改信息
    :param customer_id:
    :param customer_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(Customer, customer_id, customer_data)


def delete_customer(customer_id, force=False):
    """
    删除信息
    :param customer_id:
    :param force:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    if force:
        return db_instance.delete(Customer, customer_id)
    else:
        data = {
            'status_delete': True,
            'delete_time': datetime.datetime.utcnow()
        }
        return db_instance.edit(Customer, customer_id, data)


def get_customer_pagination(page=1, per_page=10, *args, **kwargs):
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
    rows = db_instance.get_pagination(Customer, page, per_page, *args, **kwargs)
    return rows


def delete_customer_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(Customer)


def count_customer(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(Customer, *args, **kwargs)


def get_customer_detail_info(customer_id):
    """
    获取详情
    :param customer_id:
    :return: None/object
    """
    # 客户详情
    customer_info = db_instance.get_row_by_id(Customer, customer_id)

    if not customer_info:
        return None

    # 联系方式
    customer_contact_list = get_customer_contact_rows(cid=customer_id)
    customer_info.customer_contacts = customer_contact_list

    # 开票资料
    customer_invoice = get_customer_invoice_row_by_id(customer_id)
    customer_info.customer_invoice = customer_invoice

    return customer_info
