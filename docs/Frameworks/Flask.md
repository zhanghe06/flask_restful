# Flask

https://github.com/pallets/flask

http://flask.pocoo.org/

单线程, 同步


Flask可以开启多线程，不过生产环境还是要用Nginx才行
```
if __name__ == '__main__':
    app.run(host='*.*.*.*', port=80,threaded=True)
```
