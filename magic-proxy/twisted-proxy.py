#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import re
import webbrowser

from lxml import html
from twisted.internet import defer, reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web import server, resource
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.web.server import NOT_DONE_YET

IGNORED_TAGS = ['script', 'style', 'html', 'link', 'meta', 'head']
PROXY_PORT = 8232
URL = 'https://habrahabr.ru'

class ResponseWriter(Protocol):
    def __init__(self, finished, response, request):
        self.finished = finished
        self.request = request
        self.response = response
        self.data = ''

    def dataReceived(self, data):
        if self.finished:
            self.data += data

    def replacewithtm(self, s):
        return re.sub(ur"\b(\w{6})\b", ur"\1\u2122", s,
                      flags=re.UNICODE)

    def tmize(self):
        doc = html.fromstring(self.data)
        nodes = doc.xpath('//*')
        
        exp = re.compile('')
        for node in nodes:
            if node is not None and not(node.tag.lower() in IGNORED_TAGS):
                try:
                    if node.text is not None: 
                        node.text = self.replacewithtm(node.text)
                    if node.tail is not None: 
                        node.tail = self.replacewithtm(node.tail)
                except:
                    print 'String replacing error for \'%s\'' % node.text
        self.data = html.tostring(doc)

    def connectionLost(self, reason):
        headers = self.response.headers
        if headers.hasHeader('Content-Type') and \
           'text/html' in ''.join(headers.getRawHeaders('Content-Type')):
            self.tmize()
        self.request.write(self.data)
        self.request.finish()
        self.finished.callback(None)

class DelayedResource(resource.Resource):
    isLeaf = True
    def __init__(self):
        self.agent = Agent(reactor)
    
    def _agentResponseCallback(self, response, request):
        finished = Deferred()
        response.deliverBody(ResponseWriter(finished, response, request))
        return finished

    def _agentErrorCallback(self, response, request):
        self.request.setResponseCode(500, "Error")
        self.request.finish()

    def render(self, request):
        d = self.agent.request(
            request.method,
            URL + request.uri,
            Headers({'User-Agent': ['Super Client!']}),
            None)
        d.addCallback(self._agentResponseCallback, request)
        d.addErrback(self._agentErrorCallback, request)
        return NOT_DONE_YET

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Habraproxy')
    parser.add_argument("--url",
        help="Website you want to tmize (default: %s)" % URL)
    parser.add_argument("--show", action='store_true',
        help="Add if you want to open standart browser with proxy start")
    parser.add_argument("--port", type=int,
        help="Port of your proxy (default: %d)" % PROXY_PORT)
    args = parser.parse_args()
    if args.url is not None:
        URL = args.url
    if args.port is not None:
        PROXY_PORT = args.port
    if args.show is not None and args.show:
        webbrowser.open('http://localhost:%d' % PROXY_PORT)
    site = server.Site(DelayedResource())
    reactor.listenTCP(PROXY_PORT, site)
    reactor.run()
