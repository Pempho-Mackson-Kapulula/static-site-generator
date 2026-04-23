from block_to_html import markdown_to_html_node
from title_extractor import extract_title
import os

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    # basepath injection (IMPORTANT for GitHub Pages)
    page = page.replace('href="/', f'href="{base_path}')
    page = page.replace('src="/', f'src="{base_path}')

    parent_dir = os.path.dirname(dest_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page)