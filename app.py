from http.server import SimpleHTTPRequestHandler, HTTPServer
from datetime import datetime

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        data_atual = datetime.now().strftime("%d/%m/%Y")
        self.wfile.write(f"{data_atual} - Maria Eduarda Alves dos Santos".encode('utf-8'))


server = HTTPServer(('0.0.0.0', 8080), MyHandler)
print("Servidor rodando em http://localhost:8080")
server.serve_forever()