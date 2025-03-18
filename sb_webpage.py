import main
import pathlib
import shutil
import os
import traceback
import sys
import json

import sb_robots
import sb_sitemap
import sb_manifest
import sb_assets
import sb_root_html
import sb_blogs_page_html
import sb_blog_page_html
import sb_about_me

def create_webpage():
    try:
        pathlib_export_directory = pathlib.Path(main.EXPORT_DIRECTORY).absolute()
        print(f"[+] Creating export path: {pathlib_export_directory}")

        if pathlib_export_directory.exists():
            shutil.rmtree(pathlib_export_directory)
        
        pathlib_export_directory.mkdir(parents=True, exist_ok=True)

        print("[+] Reading configuration files.")
        site_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "site_config.json"))
        blogs_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "blogs.json"))
        manifest_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "manifest.json"))
        main_page_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "main_page.json"))
        blogs_page_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "blogs_page.json"))
        blog_page_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "blog_page.json"))
        about_page_page_config_path = pathlib.Path(os.path.join(main.IMPORT_DIRECTORY, "about_page.json"))
        
        with open(site_config_path, "r", encoding="utf-8") as site_config_file:
            site_config_data = json.load(site_config_file)

        with open(blogs_config_path, "r", encoding="utf-8") as blogs_config_file:
            blogs_config_data = json.load(blogs_config_file)

        with open(manifest_config_path, "r", encoding="utf-8") as manifest_config_file:
            manifest_config_data = json.load(manifest_config_file)

        with open(main_page_config_path, "r", encoding="utf-8") as main_page_config_file:
            main_page_config_data = json.load(main_page_config_file)

        with open(blogs_page_config_path, "r", encoding="utf-8") as blogs_page_config_file:
            blogs_page_config_data = json.load(blogs_page_config_file)
        
        with open(blog_page_config_path, "r", encoding="utf-8") as blog_page_config_file:
            blog_page_config_data = json.load(blog_page_config_file)

        with open(about_page_page_config_path, "r", encoding="utf-8") as about_page_config_file:
            about_page_config_data = json.load(about_page_config_file)
        

        print("[+] Building webpage.")
        sb_robots.create_robots(site_config_data)
        sb_sitemap.create_sitemap(site_config_data, blogs_config_data)
        sb_manifest.create_manifest(manifest_config_path)
        sb_assets.copy_assets()
        sb_root_html.create_root_html(manifest_config_data, site_config_data, main_page_config_data)
        sb_blogs_page_html.create_blogs_html(blogs_config_path, manifest_config_data, site_config_data, blogs_page_config_data, blogs_config_data)
        sb_blog_page_html.create_all_blogs_html(manifest_config_data, site_config_data, blog_page_config_data, blogs_config_data)
        sb_about_me.create_about_html(manifest_config_data, site_config_data, about_page_config_data)
    except Exception as exception:
        print(f"[-] Error creating webpage.")
        traceback.print_exc()
        sys.exit(1)