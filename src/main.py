import os
import shutil
import sys
from copystatic import copy_directory_recursively
from page_generation import generate_pages_recursive

if __name__ == '__main__':
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    print(f"Generating site with basepath: {basepath}")

    dest_dir = "docs"

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    copy_directory_recursively("static/", dest_dir)
    generate_pages_recursive("content/", "template.html", dest_dir, basepath)
