import http.server
import socketserver
import os
import sys
import shutil
import pathlib
import json
import traceback
import urllib
import urllib.parse

import sb_webpage
# Settings
IMPORT_DIRECTORY = "./media"
TEST_SERVER_PORT = 8000
EXPORT_DIRECTORY = "./static"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=EXPORT_DIRECTORY, **kwargs)

if __name__ == "__main__":
    sb_webpage.create_webpage()

    # with socketserver.TCPServer(("", TEST_SERVER_PORT), Handler) as httpd:
    #     print(f"Serving test server at: http://localhost:{TEST_SERVER_PORT}")
    #     httpd.serve_forever()

    