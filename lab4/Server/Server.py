# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
from Translate import textEndpoint, wordsEndpoint, treeEndpoint
import json

hostName = 'localhost'
serverPort = 8040

class PythonTextServer(BaseHTTPRequestHandler):
    def do_POST(self):
        contentLength = int(self.headers['Content-Length'])
        postData = self.rfile.read(contentLength)

        jsonRequest = json.loads(postData.decode('utf-8'))
        jsonResponce = getResult(jsonRequest)
        print(jsonResponce)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(jsonResponce), 'utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header(
            'Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(PythonTextServer, self).end_headers()

def getResult(jsonRequest):
    if jsonRequest["endpoint"] == 1:
        return textEndpoint(jsonRequest["data"])
    elif jsonRequest["endpoint"] == 2:
        return wordsEndpoint(jsonRequest["data"])
    elif jsonRequest["endpoint"] == 3:
        return treeEndpoint(jsonRequest["data"])

if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), PythonTextServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped.')



