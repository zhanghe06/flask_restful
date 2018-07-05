## Flask Restful 最佳实践

服务依赖
- MariaDB
- Redis

项目依赖
```bash
pip install Flask-RESTful
pip install Flask-HTTPAuth
pip install Flask-SQLAlchemy
pip install sqlacodegen==1.1.6
pip install gunicorn
pip install eventlet
pip install mysqlclient
pip install redis
pip install requests
pip install celery
pip install grequests
```
注意: sqlacodegen==2.0有bug


本地启动
```bash
python run_service_api.py
或
gunicorn -k eventlet -w 4 -b 0.0.0.0:8000 web_api:app
```

更新 models
```bash
# 先更新表结构, 然后执行脚本自动更新 models
python gen.py web_api news
python gen.py web_api bearings
```

本项目使用的2个数据库:

[news](https://github.com/zhanghe06/news_spider/blob/master/db/schema/mysql.sql)
[bearings](https://github.com/zhanghe06/bearing_project/blob/master/db/schema/mysql.sql)


时间格式
```
fields.DateTime(dt_format=b'rfc822')
fields._rfc822(datetime(2011, 1, 1)) => "Sat, 01 Jan 2011 00:00:00 -0000"

fields.DateTime(dt_format=b'iso8601')
fields._iso8601(datetime(2012, 1, 1, 0, 0)) => "2012-01-01T00:00:00"
```


## 项目介绍

项目名称: 朴素之路

1. 前台模块
- [ ] 生活照片（列表、详情）Photo Album
- [ ] 水果蔬菜（列表、详情）Fruits and Vegetables
- [ ] 每日资讯（列表、详情）Daily News
- [ ] 传统节日
- [ ] 国际节日

2. 后台模块
- [ ] 照片管理（分类、上传、编辑）
- [ ] 果蔬管理（分类、上传、编辑）
- [ ] 资讯管理（分类、上传、编辑）


## HTTPS

https://letsencrypt.org/


## H5应用缓存、图标

[https://www.cnblogs.com/Richard-Core/p/ManifestTool.html](https://www.cnblogs.com/Richard-Core/p/ManifestTool.html)

```
<!-- Standard iPhone -->
<link rel="apple-touch-icon" sizes="57x57" href="./resource/touch-icon-iphone-114.png" />
<!-- Retina iPhone -->
<link rel="apple-touch-icon" sizes="114x114" href="./resource/touch-icon-iphone-114.png" />
<!-- Standard iPad -->
<link rel="apple-touch-icon" sizes="72x72" href="./resource/touch-icon-iphone-144.png" />
<!-- Retina iPad -->
<link rel="apple-touch-icon" sizes="144x144" href="./resource/touch-icon-iphone-144.png" />
```

## GitBook

```bash
npm install -g gitbook-cli
cd docs
gitbook init
gitbook serve
gitbook build
```

[http://localhost:4000](http://localhost:4000)


## 注意事项

1. 创建数据, 不需要手动指定创建时间和更新时间（建表时已设置当前时间）
2. 更新数据, 不需要手动指定更新时间, 数据库会自动更新（建表时已设置自动更新当前时间）
3. 删除数据, 默认软删除, 如需硬删, 需指定参数`force`
