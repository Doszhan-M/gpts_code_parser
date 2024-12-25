
# Project: GPTs Code Parser

## Overview

The GPTs Code Parser is a Python script designed to parse the structure of a given project directory. It extracts the folder and file hierarchy and reads the content of specific files based on configurable parameters. The results are saved to a user-defined output file for further analysis or documentation purposes.

## Features

- Recursively parses the project directory structure.
- Filters files and directories to include or exclude based on user-defined settings.
- Reads file contents for specified extensions or explicitly included files.
- Configurable via a `.env` file for flexible integration into various projects.
- Generates a comprehensive project overview in the output file.

## Prerequisites

- Python 3.8+
- `pydantic-settings==2.6.1` (defined in `requirements.txt`)

## Installation

1. Clone the repository or copy the script to your local machine.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the `.env` file:
   - Use `env.example` as a template to create your `.env` file.
   - Define paths, filters, and other configurations.

## Usage

### Configure your `.env` file:

Settings are managed via the `.env` file or can be modified directly in `src/settings.py`. Below are the key settings:

- **`project_path`**: Base directory of the project to analyze.
- **`output_file_path`**: Path to the file where results will be saved.
- **`extensions`**: List of file extensions to include.
- **`exclude_dirs`**: Directories to exclude from processing.
- **`exclude_files`**: Files to exclude from processing.
- **`include_files`**: Specific files to always include, regardless of extension.

### Run the script:

```bash
python main.py
```

The script will process the project directory and save the results to the file specified in `OUTPUT_FILE_PATH`.


## Output Format

The output file contains:

### Project Structure

A hierarchical list of directories and their contents.

### File Contents

The contents of specified files based on the filters provided.

**Example:**

```markdown
### Project Structure ###
.:
  - README.md
  - main.py

src:
  - settings.py
  - funcs.py

### File Contents ###

--- README.md ---
# GPTs Code Parser
The script parses...

--- main.py ---
from src.settings import ...
```

## Contributing

Feel free to fork the repository, make changes, and submit a pull request. Bug fixes, improvements, and additional features are welcome!
