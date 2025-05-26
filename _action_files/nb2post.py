"""
Converts Jupyter notebooks from a specified directory (default: '_notebooks')
to markdown posts compatible with static site generators like Jekyll or MkDocs.

The script performs the following main operations:
1.  Iterates through all `.ipynb` files in the input notebooks directory.
2.  For each notebook:
    a.  Determines an output sub-folder name based on the notebook's filename
        (either from a YYYY-MM-DD-name pattern or the filename stem).
    b.  Extracts metadata (title, categories, date) from the notebook:
        - Title and categories are parsed from the first markdown cell.
        - Date is extracted from the filename (if in YYYY-MM-DD format).
    c.  Uses `nbconvert` to convert the notebook content to markdown.
        - The first markdown cell (if used for metadata) is removed from the
          content before conversion.
        - Images and outputs from code cells are extracted and saved into an 'images'
          subfolder within the post's output directory.
    d.  Constructs YAML frontmatter using the extracted metadata.
    e.  Combines the frontmatter, converted markdown body, and a '<!-- more -->' tag.
    f.  Saves the final markdown content as 'index.md' in the respective
        output sub-folder within the 'converted_posts' directory.
"""
import os
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
import logging
import copy # For deepcopying notebook content
import json # For reading notebook files
import os # Potentially for path manipulations, though pathlib is primary
import re # For regex operations on filenames and content
import subprocess # If any external commands were needed (currently not used, but kept for future)

# Third-party imports
import nbformat # For converting dict to NotebookNode
import nbconvert
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ExtractOutputPreprocessor
from traitlets.config import Config as NbConvertConfig # Aliased

# Global variables for directory paths
NOTEBOOKS_DIR = Path('_notebooks')
OUTPUT_DIR = Path('converted_posts')

# Initial check for NOTEBOOKS_DIR (keep this for early exit)
# Logging will be configured in __main__, so this print is acceptable for early critical error
if not (NOTEBOOKS_DIR.exists() and NOTEBOOKS_DIR.is_dir()):
    # Consider logging.critical here if logging was configured before this point
    print(f"CRITICAL: Notebooks directory '{NOTEBOOKS_DIR}' not found. Exiting.")
    exit(1)

# Old code (related to nbdev/fastpages) has been removed.
# - _nb2htmlfname function
# - warnings set and its processing loop
# - Direct call to export2html.notebook2html
# - Imports for nbdev and fast_template


def process_notebooks():
    """
    Processes all Jupyter notebooks found in the `NOTEBOOKS_DIR`.

    For each notebook, it performs the following steps:
    1.  Derives an output folder name from the notebook's filename.
    2.  Creates the corresponding output folder and an 'images' subfolder within it.
    3.  Reads the notebook content.
    4.  Extracts metadata (title, categories from the first markdown cell; date from filename).
    5.  Prepares the notebook content for conversion (optionally removing the first cell if it was used for metadata).
    6.  Configures and uses `nbconvert.MarkdownExporter` to convert the notebook to markdown
        and extract associated outputs (like images).
    7.  Saves any extracted image files to the 'images' subfolder.
    8.  Constructs YAML frontmatter using the extracted metadata.
    9.  Assembles the final markdown string (frontmatter + body + '<!-- more -->').
    10. Writes the result to an 'index.md' file in the notebook's specific output folder.

    Side effects:
    - Creates the `OUTPUT_DIR` if it doesn't exist.
    - Creates subdirectories within `OUTPUT_DIR` for each processed notebook.
    - Creates `index.md` files and potentially image files within these subdirectories.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True) # Ensure the main output directory exists

    for notebook_path in NOTEBOOKS_DIR.glob('*.ipynb'):
        base_filename = notebook_path.name
        # Derive output folder name:
        # Attempts to match 'YYYY-MM-DD-folder-name.ipynb' pattern.
        # If matched, 'folder-name' is used. Otherwise, the notebook's stem (filename without extension) is used.
        match = re.fullmatch(r"\d{4}-\d{2}-\d{2}-(.+)\.ipynb", base_filename)
        if match:
            folder_name = match.group(1)
        else:
            # Fallback to filename stem if regex doesn't match
            folder_name = notebook_path.stem 
            # Optionally, log a warning here if proper naming is critical
            logging.warning(f"Notebook '{base_filename}' does not follow the YYYY-MM-DD-Name.ipynb naming convention. Using stem: '{folder_name}'.")

        notebook_output_folder = OUTPUT_DIR / folder_name
        notebook_output_folder.mkdir(parents=True, exist_ok=True)

        images_dir = notebook_output_folder / 'images'
        images_dir.mkdir(parents=True, exist_ok=True)

        logging.info(f"Processing notebook: {notebook_path} -> {notebook_output_folder}")

        # Read Notebook Content
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_dict = json.load(f) # Load as dict first

        # Convert the loaded dictionary to an nbformat.NotebookNode object
        # Using NO_CONVERT as we assume notebooks are in a modern format (e.g., v4)
        try:
            notebook_node = nbformat.reads(json.dumps(notebook_dict), as_version=nbformat.NO_CONVERT)
        except Exception as e:
            logging.error(f"Error converting dict to NotebookNode for {notebook_path.name}: {e}")
            continue # Skip this notebook if conversion fails

        # Extract Date from Filename
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", notebook_path.name)
        if date_match:
            date_from_filename = date_match.group(1)
        else:
            logging.warning(f"Could not extract date from filename: {notebook_path.name}. Using None.")
            date_from_filename = None
        
        # Get Current Timestamp
        current_timestamp = datetime.now().isoformat()

        # Initialize Metadata Variables
        title = notebook_path.stem # Default title to filename stem if not found in cell
        categories = []
        first_cell_was_markdown_for_meta = False # Flag to track if the first cell was processed for metadata

        # --- Metadata Extraction from First Markdown Cell ---
        # Check if the notebook has cells and the first cell is markdown.
        # Now operate on notebook_node.cells
        if (notebook_node.cells and 
            len(notebook_node.cells) > 0 and 
            notebook_node.cells[0]['cell_type'] == 'markdown'):
            first_cell_was_markdown_for_meta = True # Mark that the first cell is being parsed for metadata
            
            # The 'source' of a markdown cell can be a list of strings or a single string. Join if it's a list.
            first_cell_source = notebook_node.cells[0]['source']
            if isinstance(first_cell_source, list): # Source is usually a list of lines
                first_cell_text = "".join(first_cell_source)
            else: # In case it's a single string
                first_cell_text = first_cell_source
            
            lines = first_cell_text.splitlines()
            for line in lines:
                line_stripped = line.strip()
                if line_stripped.startswith("# "):
                    title = line_stripped[2:].strip()
                elif line_stripped.lower().startswith("- categories:") or \
                     line_stripped.lower().startswith("categories:"):
                    
                    raw_categories_str = line_stripped.split(":", 1)[1].strip()
                    parsed_as_json = False # Flag to indicate if JSON parsing was successful

                    if not raw_categories_str: # Handle empty category string
                        categories = []
                        parsed_as_json = True # Effectively, yes, resulted in empty list
                    elif raw_categories_str.startswith('[') and raw_categories_str.endswith(']'):
                        parsable_category_str = raw_categories_str.replace("'", '"') # Allow single quotes in list
                        try:
                            parsed_cats = json.loads(parsable_category_str)
                            if isinstance(parsed_cats, list):
                                categories = parsed_cats # Keep as is, will be stringified and stripped later
                                parsed_as_json = True
                            else:
                                # If json.loads results in a single item (e.g. "['foo']" might become "foo")
                                categories = [parsed_cats] 
                                parsed_as_json = True
                        except json.JSONDecodeError:
                            logging.warning(
                                f"Could not parse categories list: '{raw_categories_str}' from notebook "
                                f"'{notebook_path.name}' using JSON (even after quote replacement). "
                                f"Falling back to comma separation."
                            )
                            # Fall through to comma separation by leaving parsed_as_json = False
                    
                    if not parsed_as_json: # If not bracketed, or if JSON parsing failed
                        categories = [c.strip() for c in raw_categories_str.split(',') if c.strip()]
                    
                    # Final cleanup: ensure all are strings and stripped, and filter out empty strings
                    categories = [str(c).strip() for c in categories if str(c).strip()]
                    
                    # Categories are assumed to be defined on a single line and only once in the first cell.
                    break 

        logging.info(f"Extracted - Title: {title}, Categories: {categories}, Date: {date_from_filename}, Created: {current_timestamp}")

        # --- Prepare Notebook for Conversion ---
        # If the first markdown cell was used for metadata, it's removed from the content
        # before converting to prevent metadata (title, categories) from appearing in the post body.
        # A deepcopy of the NotebookNode is used.
        node_to_convert = notebook_node 
        if first_cell_was_markdown_for_meta:
            logging.info(f"First cell was markdown for metadata, removing it from conversion input for {notebook_path.name}")
            temp_notebook_node = copy.deepcopy(notebook_node)
            if temp_notebook_node.cells: # Double-check cells exist before pop
                temp_notebook_node.cells.pop(0) # Remove the first cell from the NotebookNode
            node_to_convert = temp_notebook_node
        else:
            logging.info(f"First cell not markdown or no cells, using original NotebookNode for {notebook_path.name}")

        # --- Configure nbconvert for Markdown Export and Image Extraction ---
        nb_config = NbConvertConfig()
        # `ExtractOutputPreprocessor` is crucial for pulling out images and other outputs.
        nb_config.MarkdownExporter.preprocessors = [ExtractOutputPreprocessor]
        # Define the template for naming extracted files (e.g., images).
        # This places images in an 'images' subdirectory relative to where the markdown file will be.
        # Example: "images/output_1_0.png"
        nb_config.ExtractOutputPreprocessor.output_filename_template = "images/{unique_key}_{cell_index}_{index}{extension}"
        
        exporter = MarkdownExporter(config=nb_config)

        # --- Perform Notebook to Markdown Conversion ---
        try:
            # `from_notebook_node` now receives a NotebookNode object.
            # `resources` will contain extracted files, like images.
            markdown_body, resources = exporter.from_notebook_node(node_to_convert)
        except Exception as e:
            logging.error(f"Error converting notebook {notebook_path.name} with nbconvert: {e}")
            continue # Skip to the next notebook

        # --- Save Extracted Files (Images) ---
        # `resources['outputs']` contains a dictionary of filenames and their binary data.
        # The `images_dir` (e.g., `converted_posts/My-Post/images/`) is where images will be saved.
        if 'outputs' in resources:
            for file_name_in_resource, file_data in resources.get('outputs', {}).items():
                # `file_name_in_resource` is typically "images/some_output_1_0.png" due to output_filename_template.
                # We extract just the filename part for saving.
                actual_image_filename = Path(file_name_in_resource).name
                output_image_path = images_dir / actual_image_filename
                
                try:
                    # Ensure the specific image directory exists (it should already from earlier mkdir).
                    output_image_path.parent.mkdir(parents=True, exist_ok=True) 
                    with open(output_image_path, 'wb') as f_image: # Write in binary mode
                        f_image.write(file_data)
                    logging.info(f"Saved extracted image: {output_image_path}")
                except Exception as e:
                    logging.error(f"Error saving image {output_image_path} for notebook {notebook_path.name}: {e}")
        
        # --- Construct YAML Frontmatter ---
        # Format categories as a YAML list of strings, e.g., ["tech", "python"].
        categories_yaml_str = '[' + ', '.join(f'"{cat}"' for cat in categories) + ']' if categories else '[]'
        # Sanitize title for YAML: replace double quotes to prevent breaking the string.
        yaml_title = title.replace('"', '“') 

        frontmatter_string = f"""---
title: "{yaml_title}"
date: "{date_from_filename if date_from_filename else current_timestamp.split('T')[0]}" # Use YYYY-MM-DD from filename or current date
created_at: "{current_timestamp}" # ISO format timestamp of processing
last_modified: "{current_timestamp}" # ISO format timestamp of processing
categories: {categories_yaml_str}
---"""

        # --- Assemble Final Markdown Content ---
        # Combine frontmatter, the converted markdown body, and a "<!-- more -->" tag for summaries.
        final_markdown_content = frontmatter_string + "\n\n" + markdown_body + "\n\n<!-- more -->"

        # --- Save the Final Markdown File ---
        output_md_path = notebook_output_folder / "index.md" # Output as index.md for clean URLs
        try:
            with open(output_md_path, 'w', encoding='utf-8') as f_md:
                f_md.write(final_markdown_content)
            logging.info(f"Successfully created Jekyll post: {output_md_path}")
        except Exception as e:
            logging.error(f"Error writing final markdown to {output_md_path} for notebook {notebook_path.name}: {e}")


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    # The NOTEBOOKS_DIR check is already done at the top for an early exit.
    # If we reach here, NOTEBOOKS_DIR is valid.
    process_notebooks()
