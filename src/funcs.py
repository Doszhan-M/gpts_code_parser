import os
from typing import List, Dict, Generator, Any


def build_project_structure(
    path: str, exclude_dirs: List[str], exclude_files: List[str]
) -> Dict[str, List[str]]:
    """Function to build the project structure"""

    structure: Dict[str, List[str]] = {}
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        relative_root: str = os.path.relpath(root, start=path)
        structure[relative_root] = []
        for filename in files:
            if filename not in exclude_files:
                structure[relative_root].append(filename)
    return structure


def collect_files(
    path: str,
    extensions: List[str],
    exclude_dirs: List[str],
    exclude_files: List[str],
    include_files: List[str],
) -> Generator[Dict[str, Any], None, None]:
    """Function to collect files"""

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for filename in files:
            if filename in exclude_files:
                continue
            if (
                any(filename.endswith(ext) for ext in extensions)
                or filename in include_files
            ):
                file_path: str = os.path.join(root, filename)
                try:
                    relative_path: str = os.path.relpath(file_path, start=path)
                    with open(file_path, "r", encoding="utf-8") as file:
                        content: str = file.read()
                    yield {"filename": relative_path, "content": content}
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
