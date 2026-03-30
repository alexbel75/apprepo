from http.server import HTTPServer, SimpleHTTPRequestHandler



class MyHandler(SimpleHTTPRequestHandler):
     def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))




def run_server(port=8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
