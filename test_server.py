from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from string import Template
import re
import os


template = Template(
    """\
<html lang="ja">
  <head>
    <title>web-font-splitter test</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" type="text/css" href="output/font-face.css" />
    <style>
      body {
        font-family: "${font_family}";
        font-size: 48px;
      }
    </style>
  </head>
  <body>
    あのイーハトーヴォのすきとおった風、<br />
    夏でも底に冷たさをもつ青いそら、<br />
    うつくしい森で飾られたモリーオ市、<br />
    郊外のぎらぎらひかる草の波。
  </body>
</html>
"""
)

with open("output/font-face.css", "r") as file:
    content = file.read()
pattern = r"^\s*font-family:\s+\"([^\"]+)\";$"
font_family = re.search(pattern, content, flags=re.MULTILINE).group(1)

html = template.substitute(font_family=font_family)


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        path = "./" + self.path[1:]
        if os.path.exists(path):
            self.send_response(200)
            if path.endswith(".css"):
                self.send_header("Content-type", "text/css; charset=utf-8")
            elif path.endswith(".woff2"):
                self.send_header("Content-type", "font/woff2")
            else:
                self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            with open(path, "rb") as f:
                self.wfile.write(f.read())
            return

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"File Not Found")


server_address = ("localhost", 8080)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()
