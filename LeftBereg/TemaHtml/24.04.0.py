from http.server import BaseHTTPRequestHandler,HTTPServer
class SimpleHadler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        html_content = """"
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Простой сервер</title>
        </head>
        <body>
            <h1> Привет! Это простая HTML страница </h1>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode("utf-8"))
serverAddress = ('',8080)
httpd = HTTPServer(serverAddress,SimpleHadler)
print(f'Сервер запущен на http://localhost:{8080}')
httpd.serve_forever()
