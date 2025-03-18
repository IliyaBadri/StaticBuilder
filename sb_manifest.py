import main
import os
import traceback
import sys
import shutil

def create_manifest(manifest_config_path: str):
    try:
        json_directory = os.path.abspath(os.path.join(main.EXPORT_DIRECTORY, "json"))
        manifest_path = os.path.join(json_directory, "manifest.json")
        print(f"[+] Creating {manifest_path}")
        os.makedirs(json_directory, exist_ok=True)
        shutil.copy(manifest_config_path, manifest_path)
    except Exception as exception:
        print(f"[-] Error creating {manifest_path}")
        traceback.print_exc()
        sys.exit(1)