import main
import os
import traceback
import sys

def create_robots(site_config_data: dict):
    try:
        robots_path = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, "robots.txt"))
        print(f"[+] Creating {robots_path}")
        with open(robots_path, "w") as robots_file:
            contents = f"""User-agent: *
Sitemap: https://{site_config_data["domain"]}/sitemap.xml
"""
            robots_file.write(contents)
    except Exception as exception:
        print(f"[-] Error creating {robots_path}")
        traceback.print_exc()
        sys.exit(1)