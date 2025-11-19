import os
import shutil
from copystatic import copy_directory_recursively
from page_generation import generate_pages_recursive

if __name__ == '__main__':
    if os.path.exists("public/"):
        shutil.rmtree("public/")

    print("Copying static files...")
    copy_directory_recursively("static/", "public/")

    print("Generating content...")
    generate_pages_recursive("content/", "template.html", "public/")
