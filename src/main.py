from copy_content import copy_static
from page_generator import generate_page
import os

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    src_path = os.path.join(BASE_DIR, "static")
    dst_path = os.path.join(BASE_DIR, "public")

    copy_static(src_path, dst_path)

    generate_page(
        from_path=os.path.join(BASE_DIR, "content/index.md"),
        template_path=os.path.join(BASE_DIR, "template.html"),
        dest_path=os.path.join(BASE_DIR, "public/index.html")
    )


if __name__ == "__main__":
    main()