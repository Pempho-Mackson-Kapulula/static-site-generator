from copy_content import copy_static
from recursive_page_generator import generate_pages_recursive
import os

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    src_path = os.path.join(BASE_DIR, "static")
    dst_path = os.path.join(BASE_DIR, "public")

    copy_static(src_path, dst_path)

    generate_pages_recursive(
        dir_path_content=os.path.join(BASE_DIR, "content"),
        template_path=os.path.join(BASE_DIR, "template.html"),
        dest_dir_path=os.path.join(BASE_DIR, "public")
    )


if __name__ == "__main__":
    main()