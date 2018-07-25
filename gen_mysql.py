#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

from config import current_config

BASE_DIR = current_config.BASE_DIR
# SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI
SQLALCHEMY_BINDS = current_config.SQLALCHEMY_BINDS


def gen_models(app_name, db_key):
    """
    创建 models 支持多库
    :param app_name:
    :param db_key:
    :return:
    """
    file_path = os.path.join(BASE_DIR, app_name, 'models', '%s.py' % db_key)
    cmd = 'sqlacodegen %s --noinflect --outfile %s' % (SQLALCHEMY_BINDS[db_key], file_path)
    print(cmd)

    output = os.popen(cmd)
    result = output.read()
    print(result)

    # 更新 model 文件
    with open(file_path, b'r') as f:
        lines = f.readlines()
    # 替换 model 关键内容
    lines[2] = b'from %s.databases.%s import db\n' % (app_name, db_key)
    lines[5] = b'Base = db.Model\n'

    # 新增 model 转 dict 方法
    with open(file_path, b'w') as f:
        lines.insert(9, b'def to_dict(self):\n')
        lines.insert(10, b'    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}\n')
        lines.insert(11, b'\n')
        lines.insert(12, b'Base.to_dict = to_dict\n')
        lines.insert(13, b'Base.__bind_key__ = \'%s\'\n' % db_key)
        lines.insert(14, b'\n\n')
        f.write(b''.join(lines))


def usage():
    print('''
创建/更新 models
$ python gen_mysql.py [项目名称] [数据库键]
$ python gen_mysql.py web_api news
$ python gen_mysql.py web_api bearings
''')


def run():
    """
    入口
    """
    # print sys.argv
    try:
        if len(sys.argv) < 3:
            raise Exception('缺失参数\n')
        gen_models(sys.argv[1], sys.argv[2])
    except Exception as e:
        print(e.message)
        usage()


if __name__ == '__main__':
    run()
    # print(BASE_DIR)
    # print(SQLALCHEMY_DATABASE_URI)
