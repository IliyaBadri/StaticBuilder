import main
import traceback
import sys
import os
import urllib

def create_sitemap(site_config_data: dict, blogs_config_data: dict):
    try:
        sitemap_path = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, "sitemap.xml"))
        print(f"[+] Creating {sitemap_path}")

        blog_dicts = blogs_config_data["blogs"]

        blog_path_xmls = ""

        for blog_dict in blog_dicts:
            blog_path_xmls += f"""<url>
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