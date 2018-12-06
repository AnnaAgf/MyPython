#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

# This class will handles any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World!') # Send the html message
        return

try:
    # Create a web server and define the handler to manage the incoming request
    server = HTTPServer(("localhost", 8081), myHandler)
    print 'Started http server on port ', 8081
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
