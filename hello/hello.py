#!/usr/bin/env python
# coding:utf-8

import http.server
from prometheus_client import start_http_server
import random
from prometheus_client import Counter
from prometheus_client import Gauge

REQUESTS = Counter('hello_worlds_total',
        'Hello Worlds requested.')
EXCEPTIONS = Counter('hello_world_exceptions_total',
        'Exceptions serving Hello World.')
LAST = Gauge('hello_world_last_time_seconds',
        'The last time a Hello World was served.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        with EXCEPTIONS.count_exceptions():
          if random.random() < 0.2:
            raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")
        LAST.set_to_current_time()

if __name__ == "__main__":
    start_http_server(8001)
    server = http.server.HTTPServer(('', 8002), MyHandler)
    server.serve_forever()
