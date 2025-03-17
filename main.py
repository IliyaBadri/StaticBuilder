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

# Settings
IMPORT_DIRECTORY = "./media"
TEST_SERVER_PORT = 8000
EXPORT_DIRECTORY = "./static"

def create_robots(site_config_data):
    robots_path = os.path.join(EXPORT_DIRECTORY, "robots.txt")
    try:
        
        with open(robots_path, "w") as robots_file:
            
            contents = f"""User-agent: *
Sitemap: https://{site_config_data["domain"]}/sitemap.xml
"""
            robots_file.write(contents)
    except Exception as exception:
        print(f"[-] Error creating {robots_path}")
        traceback.print_exc()
        sys.exit(1)


def create_sitemap(site_config_data, blogs_config_data):
    try:
        sitemap_path = os.path.join(EXPORT_DIRECTORY, "sitemap.xml")
        blog_dicts = blogs_config_data["blogs"]

        blog_path_xmls = ""

        for blog_dict in blog_dicts:
            blog_path_xmls += f"""
<url>
    <loc>{urllib.parse.urljoin(f"https://{site_config_data["domain"]}", blog_dict["path"])}</loc>
</url>
"""
        with open(sitemap_path, "w") as sitemap_file:
            contents = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
    <loc>https://{site_config_data["domain"]}/</loc>
</url>
{blog_path_xmls}
</urlset>
"""
            sitemap_file.write(contents)
    except Exception as exception:
        print(f"[-] Error creating {sitemap_path}")
        traceback.print_exc()
        sys.exit(1)
    
def create_main_page():
    pass 



def create_webpage():
    try:
        pathlib_export_directory = pathlib.Path(EXPORT_DIRECTORY)

        if pathlib_export_directory.exists():
            shutil.rmtree(pathlib_export_directory)
        
        pathlib_export_directory.mkdir(parents=True, exist_ok=True)

        site_config_path = pathlib.Path(os.path.join(IMPORT_DIRECTORY, "site_config.json"))
        blogs_config_path = pathlib.Path(os.path.join(IMPORT_DIRECTORY, "blogs.json"))
        
        with open(site_config_path, "r", encoding="utf-8") as site_config_file:
            site_config_data = json.load(site_config_file)

        with open(blogs_config_path, "r", encoding="utf-8") as blogs_config_file:
            blogs_config_data = json.load(blogs_config_file)

        create_robots(site_config_data)
        create_sitemap(site_config_data, blogs_config_data)
    except Exception as exception:
        print(f"[-] Error creating webpage.")
        traceback.print_exc()
        sys.exit(1)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=EXPORT_DIRECTORY, **kwargs)

if __name__ == "__main__":
    create_webpage()

    # with socketserver.TCPServer(("", TEST_SERVER_PORT), Handler) as httpd:
    #     print(f"Serving test server at: http://localhost:{TEST_SERVER_PORT}")
    #     httpd.serve_forever()

    