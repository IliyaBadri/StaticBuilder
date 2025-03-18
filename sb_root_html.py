import urllib.parse
import main
import traceback
import sys
import os
import urllib

def create_root_html(manifest_config_data: dict, site_config_data: dict, main_page_config_data: dict):
    try:
        root_html_path = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, "index.html"))
        print(f"[+] Creating {root_html_path}")

        with open(root_html_path, "w") as root_html_file:
            contents = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="{manifest_config_data["theme_color"]}">
  <meta name="description" content="{main_page_config_data["root_description"]}">

  <meta property="og:title" content="{manifest_config_data["name"]}">
  <meta property="og:description" content="{main_page_config_data["root_description"]}">
  <meta property="og:image" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", "/images/favicon.png")}">
  <meta property="og:url" content="https://{site_config_data["domain"]}/">
  <meta property="og:type" content="website">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{manifest_config_data["name"]}">
  <meta name="twitter:description" content="{main_page_config_data["root_description"]}">
  <meta name="twitter:image" content="{urllib.parse.urljoin(f"https://{site_config_data["domain"]}/", "/images/favicon.png")}">

  <link rel="shortcut icon" href="/images/favicon.png" type="image/png">
  <link rel="manifest" href="/json/manifest.json">
  <link href="/css/tailwind.css" rel="stylesheet">
  <title>{manifest_config_data["name"]}</title>
  <style>
    body {{
      height: 100vh;
      overflow: hidden;
    }}
  </style>
</head>
<body class="bg-white flex flex-col items-center justify-center text-gray-800">
  <nav class="w-full fixed top-0 left-0 bg-white shadow-md p-4 flex justify-between items-center mx-auto">
    <button onclick="window.location.href='/'" class="text-xl font-semibold">{manifest_config_data["name"]}</button>
    <div class="space-x-4">
      <button onclick="window.location.href='/about'" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">{main_page_config_data["about_navbar_button_text"]}</button>
      <button onclick="window.location.href='/blogs'" class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300">{main_page_config_data["blogs_navbar_button_text"]}</button>
    </div>
  </nav>
  <div class="flex flex-col items-center text-center">
    <h1 class="text-3xl md:text-5xl font-bold">{main_page_config_data["hero_title"]}</h1>
    <p class="text-lg md:text-xl text-gray-600 mt-2">{main_page_config_data["hero_description"]}</p>
    <button onclick="window.location.href='/about'" class="mt-4 px-6 py-3 bg-gray-800 text-white rounded-lg hover:bg-gray-700">{main_page_config_data["hero_about_button_text"]}</button>
  </div>
</body>
</html>
"""
            root_html_file.write(contents)
    except Exception as exception:
        print(f"[-] Error creating {root_html_path}")
        traceback.print_exc()
        sys.exit(1)