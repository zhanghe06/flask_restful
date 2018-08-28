# Flask-RESTful

官方文档: [http://flask-restful.readthedocs.io/en/latest/quickstart.html](http://flask-restful.readthedocs.io/en/latest/quickstart.html)


关键组件:

- 注册蓝图
- 注册路由
- 参数解析
- 输出过滤



## 注册蓝图
```
# 定义蓝图
network_bp = Blueprint('network', __name__, url_prefix='/network')
compute_bp = Blueprint('compute', __name__, url_prefix='/compute')

# 定义接口
network_api = Api(network_bp, errors=errors)
compute_api = Api(compute_bp, errors=errors)

# 注册蓝图
app.register_blueprint(network_bp)
app.register_blueprint(compute_bp)
```

## 注册路由

```
api.add_resource(FetchResultResource, '/fetch_result/<int:pk>', endpoint='fetch_result', strict_slashes=False)
```
strict_slashes=False  取消严格斜杠语法, 请求忽略最后斜杠, 不做跳转



## 参数解析（Request Parsing）
```
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name')
parser.add_argument('name_original', dest='public_name')
parser.add_argument('name_list', action='append')
args = parser.parse_args()
```

参数说明

参数 | 默认值 | 说明
--- | --- | ---
default | None | 默认值
dest | None | 参数名称转换
required | False | 是否必填（True/False）
ignore | False | 是否忽略参数类型转换失败的情况
type | text_type | 默认字符类型, 可添加自定义类型
location | ('json', 'values',) | 参数解析来源
choices | () | 参数允许范围
action | 'store' | 参数直接处理, 若为'append'则将参数当列表处理
help | None | 参数错误提示
operators | ('=',) | 操作符
case_sensitive | True | 大小写敏感
store_missing | True | 如果请求参数缺失, 是否存储默认值
trim | False | 是否去除前后空字符
nullable | True | 是否允许传None值


## 输出过滤（Output Fields）

字段说明
```
fields.Integer                              # 整数格式
fields.String                               # 字符串
fields.DateTime(dt_format='iso8601')        # 日期时间
fields.Url('api_resource_endpoint')         # 资源链接
fields.List(custom_fields)                  # 列表格式
fields.Nested(custom_fields)                # 字典嵌套
fields.List(fields.Nested(custom_fields))   # 列表嵌套
```

可选参数
```
fields.String(attribute='another_name')     # 重名名
fields.String(default='default_value')      # 默认值
```

输出过滤

参数说明
```
marshal(data, fields, envelope=None)

data: 原始数据
fields: 过滤格式
envelope: 包装字段
```

例子
```
>>> from flask_restful import fields, marshal
>>> data = { 'a': 100, 'b': 'foo' }
>>> mfields = { 'a': fields.Raw }

>>> marshal(data, mfields)
OrderedDict([('a', 100)])

>>> marshal(data, mfields, envelope='data')
OrderedDict([('data', OrderedDict([('a', 100)]))])
```

关于嵌套结构的示例

1、嵌套结构有数据

![bearings customer info with contact](https://github.com/zhanghe06/flask_restful/raw/master/images/postman_bearings_customer_info_with_contact.png)

2、嵌套结构无数据

![bearings customer info without contact](https://github.com/zhanghe06/flask_restful/raw/master/images/postman_bearings_customer_info_without_contact.png)
