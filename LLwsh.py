#! /usr/bin/python
# -*- coding: UTF-8 -*-

from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler
port = 80
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default
server = HTTPServer(('localhost', port), handler)
print("Starting my web server on port "+str(port))
server.serve_forever()