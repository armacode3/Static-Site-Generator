import os
import shutil
from pathlib import Path
from markdown_html import markdown_to_html_node

from markdown_html import markdown_to_html_node

def extract_title(markdown):
    markdown_lines = markdown.split("\n")

    for line in markdown_lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown_contents = f.read()

    with open(template_path) as f:
        html_contents = f.read()

    mark_to_html = markdown_to_html_node(markdown_contents).to_html()

    title = extract_title(markdown_contents)

    full_html = (html_contents.replace("{{ Title }}", title).replace("{{ Content }}", mark_to_html))


    dirpath = os.path.dirname(dest_path)
    
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)

        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path)
        
        else:
            generate_pages_recursive(from_path, template_path, dest_path)