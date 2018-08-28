# Flask

https://github.com/pallets/flask

http://flask.pocoo.org/

单线程, 同步

Flask 自带的`server`是`werkzeug`, 默认的`werkzeug`是单线程

生产环境下，通过`uwsgi`或者`gunicorn`实现多线程方式


Flask本身也可以开启多线程，不过生产环境还是要用Nginx才行
```
if __name__ == '__main__':
    app.run(host='*.*.*.*', port=80, threaded=True)
```
