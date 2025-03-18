import main
import os
import traceback
import sys
import shutil

def copy_assets():
    try:
        assets_directory = os.path.abspath(os.path.join(main.IMPORT_DIRECTORY, "assets"))
        export_root_directory = os.path.abspath(main.EXPORT_DIRECTORY)
        print(f"[+] Copying assets into {export_root_directory}")
        shutil.copytree(assets_directory, export_root_directory, dirs_exist_ok=True)
    except Exception as exception:
        print(f"[-] Error copying assets into {export_root_directory}")
        traceback.print_exc()
        sys.exit(1)