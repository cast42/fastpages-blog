import unittest
from pathlib import Path
import shutil
import json
from datetime import datetime
import sys
import re # For checking timestamps

# Add the parent directory of 'nb2post' to sys.path to allow direct import
# This assumes 'test_nb2post.py' and 'nb2post.py' are in the same directory '_action_files'
# and this script is run from the root of the repository.
# For a more robust solution, especially if running tests from different locations,
# Python packaging or PYTHONPATH adjustments might be better.
# However, for this specific setup, relative import is preferred.
try:
    from . import nb2post
except ImportError:
    # Fallback if running the test script directly and '.' isn't on the path
    # Or if the above relative import fails in the execution environment.
    sys.path.append(str(Path(__file__).parent.resolve()))
    import nb2post


# Sample Notebook Data
SAMPLE_NOTEBOOK_FILENAME = "2023-01-01-Test-Notebook.ipynb"
SAMPLE_NOTEBOOK_CONTENT = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Test Title\n",
                "- categories: [test, sample]\n",
                "Some other descriptive text in the first cell."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        # 1x1 black pixel PNG
                        "image/png": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": "# Sample plot generation code"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "This is the main body of the notebook."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.9.1"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}


class TestNb2Post(unittest.TestCase):

    def setUp(self):
        self.test_root = Path("temp_test_nb2post_action") # Changed name slightly to avoid conflicts if run locally
        self.notebooks_dir = self.test_root / "_notebooks"
        self.converted_dir = self.test_root / "converted_posts"

        self.notebooks_dir.mkdir(parents=True, exist_ok=True)
        # self.converted_dir.mkdir(parents=True, exist_ok=True) # nb2post creates this

        # Create the sample notebook file
        with open(self.notebooks_dir / SAMPLE_NOTEBOOK_FILENAME, 'w') as f:
            json.dump(SAMPLE_NOTEBOOK_CONTENT, f)

        # Patch nb2post's global directory variables
        self.patch_notebooks_dir = unittest.mock.patch.object(nb2post, 'NOTEBOOKS_DIR', self.notebooks_dir)
        self.patch_output_dir = unittest.mock.patch.object(nb2post, 'OUTPUT_DIR', self.converted_dir)

        self.patch_notebooks_dir.start()
        self.patch_output_dir.start()
        
        # Configure logging for tests (optional, but can be helpful)
        # logging.basicConfig(level=logging.DEBUG)


    def tearDown(self):
        self.patch_notebooks_dir.stop()
        self.patch_output_dir.stop()
        if self.test_root.exists():
            shutil.rmtree(self.test_root)

    def test_conversion_process(self):
        # Run the main processing function from nb2post
        nb2post.process_notebooks()

        # Assert Folder Structure
        expected_post_folder_name = "Test-Notebook" # from "2023-01-01-Test-Notebook.ipynb"
        post_output_dir = self.converted_dir / expected_post_folder_name
        
        self.assertTrue(post_output_dir.exists(), f"Post output folder {post_output_dir} does not exist.")
        
        index_md_path = post_output_dir / "index.md"
        self.assertTrue(index_md_path.exists(), f"index.md does not exist in {post_output_dir}.")
        
        images_dir = post_output_dir / "images"
        self.assertTrue(images_dir.exists(), f"Images folder {images_dir} does not exist.")

        # Check for an image file (any PNG in this case)
        image_files = list(images_dir.glob("*.png"))
        self.assertTrue(len(image_files) > 0, f"No PNG image found in {images_dir}.")
        
        # Assert index.md Content
        with open(index_md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Frontmatter Checks
        self.assertIn('title: "Test Title"', md_content)
        self.assertIn('date: "2023-01-01"', md_content)
        # Check for categories as a YAML list: categories: "[test, sample]" or categories: ['test', 'sample']
        # The current implementation produces: categories: ["test", "sample"]
        self.assertTrue(re.search(r"categories:\s*\[\s*\"test\"\s*,\s*\"sample\"\s*\]", md_content), "Categories not found or not in correct format.")
        
        # Check for ISO timestamps for created_at and last_modified
        # Example regex: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+
        self.assertTrue(re.search(r"created_at:\s*\"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+(-[0-9:]+)?\"", md_content), "created_at timestamp missing or not in ISO format.")
        self.assertTrue(re.search(r"last_modified:\s*\"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+(-[0-9:]+)?\"", md_content), "last_modified timestamp missing or not in ISO format.")

        # Content Body Checks
        # Metadata lines from the first cell should NOT be in the body
        self.assertNotIn("# Test Title", md_content.split("---", 2)[-1], "Title from first cell found in body.")
        self.assertNotIn("- categories: [test, sample]", md_content.split("---", 2)[-1], "Categories line from first cell found in body.")
        # However, "Some other descriptive text in the first cell." SHOULD be removed as it was part of the first cell.
        self.assertNotIn("Some other descriptive text in the first cell.", md_content.split("---", 2)[-1], "Other text from first (metadata) cell found in body.")

        # Content from other cells should be present
        self.assertIn("This is the main body of the notebook.", md_content)
        
        # Check for image link (nbconvert default is ![alt text](filename))
        # The filename is like {unique_key}_{cell_index}_{index}{extension}
        self.assertTrue(re.search(r"!\[png\]\(images/[a-zA-Z0-9_]+\.png\)", md_content), "Image link not found in markdown body.")
        
        # Check for <!-- more --> tag at the end
        self.assertTrue(md_content.strip().endswith("<!-- more -->"))

if __name__ == "__main__":
    # Need to import unittest.mock for the patches to work if not already imported globally
    try:
        import unittest.mock
    except ImportError:
        # Python 2 fallback (less likely for this project)
        # import mock as mock
        pass # Assuming Python 3, unittest.mock is standard
    unittest.main()
