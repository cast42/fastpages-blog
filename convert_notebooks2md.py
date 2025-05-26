import os
import shutil
from datetime import datetime

import nbformat
from nbconvert import MarkdownExporter

NOTEBOOKS_DIR = "_notebooks"
POSTS_DIR = "converted_posts"


def parse_metadata_from_filename(filename):
    # Example: 2020-01-28-Altair.ipynb
    base = os.path.splitext(filename)[0]
    parts = base.split("-", 3)
    if len(parts) >= 4:
        date = f"{parts[0]}-{parts[1]}-{parts[2]}"
        title = parts[3].replace("-", " ")
    else:
        date = datetime.now().strftime("%Y-%m-%d")
        title = base.replace("-", " ")
    created_at = f"{date}T10:44:22.941081"
    last_modified = f"{date}T10:44:22.941087"
    return title, date, created_at, last_modified


def extract_image_paths(md_text):
    """Extract image paths from markdown text."""
    import re

    # Matches ![](path) or ![alt](path)
    return re.findall(r"!\[.*?\]\((.*?)\)", md_text)


def convert_notebook_to_markdown(notebook_path, output_dir, filename):
    # Parse metadata
    title, date, created_at, last_modified = parse_metadata_from_filename(filename)
    header = f"""---
title: {title}
date: {date}
created_at: {created_at}
last_modified: {last_modified}
---
"""
    # Load notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    # Convert to markdown
    exporter = MarkdownExporter()
    body, _ = exporter.from_notebook_node(nb)
    # Write markdown file with header and footer
    md_path = os.path.join(output_dir, "index.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(body)
        if not body.endswith("\n"):
            f.write("\n")
        f.write("<!-- more -->\n")
    return body


def copy_images(image_paths, src_dir, dest_dir):
    for img_path in image_paths:
        # Only handle local images
        if img_path.startswith("http"):
            continue
        abs_src = os.path.join(src_dir, img_path)
        abs_dest = os.path.join(dest_dir, os.path.basename(img_path))
        if os.path.exists(abs_src):
            shutil.copy2(abs_src, abs_dest)


def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    for fname in os.listdir(NOTEBOOKS_DIR):
        if fname.endswith(".ipynb"):
            notebook_path = os.path.join(NOTEBOOKS_DIR, fname)
            post_name = os.path.splitext(fname)[0]
            post_dir = os.path.join(POSTS_DIR, post_name)
            os.makedirs(post_dir, exist_ok=True)
            # Convert notebook to markdown
            md_text = convert_notebook_to_markdown(notebook_path, post_dir, fname)
            # Find and copy images
            image_paths = extract_image_paths(md_text)
            copy_images(image_paths, NOTEBOOKS_DIR, post_dir)
            print(f"Processed {fname} -> {post_dir}")


if __name__ == "__main__":
    main()
