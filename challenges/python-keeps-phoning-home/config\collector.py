import http.server
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("BEACON:", self.path, flush=True)
        self.send_response(204)
        self.end_headers()
    def log_message(self, *a):
        pass
http.server.HTTPServer(("0.0.0.0", 9999), H).serve_forever()