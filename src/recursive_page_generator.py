import os
from page_generator import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)

        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_dir_path, base_path)

        elif os.path.isfile(src_path) and src_path.endswith(".md"):
            rel_path = os.path.relpath(src_path, base_path)
            rel_path = rel_path[:-3] + ".html"

            dest_path = os.path.join(dest_dir_path, rel_path)

            generate_page(src_path, template_path, dest_path, base_path)