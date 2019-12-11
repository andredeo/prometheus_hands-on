#!/usr/bin/env python
# coding:utf-8

import urllib2
import time
import datetime
from HTMLParser import HTMLParser
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from random import randint

class myHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write('process_start_time_seconds '+ datetime.datetime.now().strftime("%s")+'\n')
    self.wfile.write('demo {type="test", id="1"} '+str(randint(0, 100)) +'\n')
    self.wfile.write('demo {type="test", id="2"} '+str(randint(0, 100)) +'\n')
    self.wfile.write('demo {type="test", id="3"} '+str(randint(0, 100)) +'\n')
    return

try:
  server = HTTPServer(('', 8000), myHandler)
  print 'Started httpserver on port 8000'
  server.serve_forever()
except KeyboardInterrupt:
  print '^C received, shutting down the web server'
  server.socket.close()
