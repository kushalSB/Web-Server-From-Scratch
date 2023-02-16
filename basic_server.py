import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"Basic Server Response!!")

with socketserver.TCPServer(("",PORT),Handler) as httpd:
    print(f'Serving ar Port {PORT}')
    httpd.serve_forever()
    