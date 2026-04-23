from copy_content import copy_static
from recursive_page_generator import generate_pages_recursive
import os
import sys

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    src_path = os.path.join(BASE_DIR, "static")
    dst_path = os.path.join(BASE_DIR, "docs")  

    copy_static(src_path, dst_path)

    generate_pages_recursive(
        dir_path_content=os.path.join(BASE_DIR, "content"),
        template_path=os.path.join(BASE_DIR, "template.html"),
        dest_dir_path=dst_path,
        base_path=base_path
    )


if __name__ == "__main__":
    main()