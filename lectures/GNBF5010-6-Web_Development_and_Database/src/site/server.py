import http.server

def run(port = 8000,
        server_class = http.server.HTTPServer,
        handler_class = http.server.SimpleHTTPRequestHandler):
    httpd = server_class(('', port), handler_class)
    httpd.serve_forever()

run()
