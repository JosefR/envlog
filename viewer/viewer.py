import sys
import http.server
import threading
import time
import os.path

class Viewer(threading.Thread):
    def __init__(self, address='0.0.0.0', port=8000):
        threading.Thread.__init__(self)
        handler_class = ViewerRequestHandler
        handler_class.protocol_version = 'HTTP/1.0'
        server_class = http.server.HTTPServer
        self.httpd = server_class((address, port), handler_class)

    def run(self):
        print('Viewer running.')
        self.httpd.serve_forever()


class ViewerRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        print('init')
        http.server.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        sensordata = ''
        if os.path.exists('sensordata'):
            with open('sensordata', 'r') as f:
                sensordata = f.read()
        r = '<html>\
            <head><title>Envlog</title></head\
            <body>\
            <p>Data: {}</p>\
            </body>\
            </html>'.format(sensordata)
        self.send_response(200) # Response 'OK'
        self.send_header("Content type", "Content-Type: text/html; charset=utf-8")
        self.send_header("Content-length", len(r))
        self.end_headers()
        self.wfile.write(r.encode('utf-8'))
        self.wfile.flush()

