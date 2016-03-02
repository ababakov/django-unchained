#!/usr/bin/env python
import tornado.ioloop
import maproxy.proxyserver

server = maproxy.proxyserver.ProxyServer("habrahabr.ru", 443,
                                          server_ssl_options=True)
server.listen(82)
print("http://127.0.0.1:82 -> https://habrahabr.com")
tornado.ioloop.IOLoop.instance().start()