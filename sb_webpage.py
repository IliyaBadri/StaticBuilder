import main
import pathlib
import shutil
import os
import sb_robots
import sb_sitemap
import traceback
import sys
import json

def create_webpage():
    try:
        pathlib_export_directory = pathlib.Path(main.EXPORT_DIRECTORY)

        if pathlib_export_directory.exists():
            shutil.rmtree(pathlib_export_directory)
        
        pathlib_export_directory.mkdir(parents=True, exist_ok=True)

        site_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "site_config.json"))
        blogs_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "blogs.json"))
        
        with open(site_config_path, "r", encoding="utf-8") as site_config_file:
            site_config_data = json.load(site_config_file)

        with open(blogs_config_path, "r", encoding="utf-8") as blogs_config_file:
            blogs_config_data = json.load(blogs_config_file)

        sb_robots.create_robots(site_config_data)
        sb_sitemap.create_sitemap(site_config_data, blogs_config_data)
    except Exception as exception:
        print(f"[-] Error creating webpage.")
        traceback.print_exc()
        sys.exit(1)