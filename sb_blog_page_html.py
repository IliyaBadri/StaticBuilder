import urllib.parse
import main
import traceback
import sys
import os
import urllib
import markdown
import datetime


def create_all_blogs_html(manifest_config_data: dict, site_config_data: dict, blog_page_config_data: dict, blogs_config_data: dict):
    try:
        for blog_data in blogs_config_data["blogs"]:
          
            blog_directory = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, blog_data["path"].lstrip("/")))
            os.makedirs(blog_directory, exist_ok=True)

            blog_html_path = os.path.join(blog_directory, "index.html")

            print(f"[+] Creating {blog_html_path}")

            content_file_path = os.path.abspath(os.path.join(main.IMPORT_DIRECTORY, blog_data["path"].lstrip("/"), "content.md"))

            with open(content_file_path, 'r', encoding='utf-8') as md_file:
              markdown_content = md_file.read()

            html_content = markdown.markdown(markdown_content, extensions=["fenced_code", "tables"])
            
            with open(blog_html_path, "w") as blog_html_file:
                contents = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="{manifest_config_data["theme_color"]}">
  <meta name="description" content="{blog_data["description"]}">

  <meta property="og:title" content="{blog_data["title"]} - {manifest_config_data["short_name"]}">
  <meta property="og:description" content="{blog_data["description"]}">
  <meta property="og:image" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", "/images/favicon.png")}">
  <meta property="og:url" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", blog_data["path"])}">
  <meta property="og:type" content="article">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{blog_data["title"]} - {manifest_config_data["short_name"]}">
  <meta name="twitter:description" content="{blog_data["description"]}">
  <meta name="twitter:image" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", "/images/favicon.png")}">

  <link rel="shortcut icon" href="/images/favicon.png" type="image/png">
  <link rel="manifest" href="/json/manifest.json">
  <link href="/css/tailwind.css" rel="stylesheet">
  <title>{blog_data["title"]} - {manifest_config_data["short_name"]}</title>
</head>
<body class="bg-white text-gray-800">
  <nav class="w-full fixed top-0 left-0 bg-white shadow-md p-4 flex justify-between items-center mx-auto">
    <button onclick="window.location.href='/'" class="text-xl font-semibold">{manifest_config_data["name"]}</button>
    <div class="space-x-4">
      <button onclick="window.location.href='/about'" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">{blog_page_config_data["about_navbar_button_text"]}</button>
      <button onclick="window.location.href='/blogs'" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">{blog_page_config_data["blogs_navbar_button_text"]}</button>
    </div>
  </nav>

  <div class="max-w-3xl mx-auto p-8 pt-24 mt-20">
    <article class="bg-white p-6 rounded-xl shadow-xl border-2 border-gray-200">
      <h1 class="text-3xl font-bold text-gray-800">{blog_data["title"]}</h1>
      <p class="text-gray-500 text-sm mt-2 mb-3">{blog_data["date"]}</p>
      <dev id="markdown" class="text-gray-700 prose max-w-none">
{html_content}
      </dev>
    </article>
  </div>
  <footer class="bg-gray-800 text-white text-center py-6 mt-8">
    <p>&copy; {datetime.datetime.now().year} {manifest_config_data["name"]}. All rights reserved.</p>
  </footer>
</body>
</html>
"""
                blog_html_file.write(contents)
            
    except Exception as exception:
        print(f"[-] Error creating blogs.")
        traceback.print_exc()
        sys.exit(1)