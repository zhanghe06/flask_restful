# Frameworks

## WSGI

`WSGI`全称是`Web Server Gateway Interface`, `WSGI`不是服务器, python模块, 框架, API或者任何软件, 只是一种规范

要实现`WSGI`协议，必须同时实现`web server`和`web application`, 当前运行在`WSGI`协议之上的web框架有`Torando`,`Flask`,`Django`


## 个人观点:

因为每个web框架都不是专注于实现服务器方面的，因此，在生产环境部署的时候使用的服务器也不会简单的使用web框架自带的服务器

所以单纯的讨论框架本身的并发性能意义不大
