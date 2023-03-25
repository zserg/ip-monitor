#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import threading
import logging
import time
from requests import get

ip = "x.x.x.x"

class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):
        #send code 200 response
        self.send_response(200)

        #send header first
        self.send_header('Content-type','text-html')
        self.end_headers()

        #send file content to client
        f = '%s'
        self.wfile.write(bytes(f % ip, "utf-8"))

def thread_function(name):
    global ip
    while True:
        try:
           ip = get('https://api.ipify.org').content.decode('utf8')
           time.sleep(10)
        except:
           ip = "x.x.x.x"
    
    
def run():
    print('http server is starting...')
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()

    #ip and port of servr
    #by default http server port is 80
    server_address = ('127.0.0.1', 5000)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()

