from src.settings import load_settings
from src.funcs import build_project_structure, collect_files


if __name__ == "__main__":
    settings = load_settings()
    output_file_path: str = "project_code.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        project_structure = build_project_structure(
            settings.project_path, settings.exclude_dirs, settings.exclude_files
        )
        output_file.write("### Project Structure ###\n")
        for directory, files in project_structure.items():
            output_file.write(f"{directory}:\n")
            for file in files:
                output_file.write(f"  - {file}\n")
            output_file.write("\n")
        output_file.write("\n### File Contents ###\n")
        for file_data in collect_files(
            settings.project_path,
            settings.extensions,
            settings.exclude_dirs,
            settings.exclude_files,
            settings.include_files,
        ):
            output_file.write(f"\n--- {file_data['filename']} ---\n")
            output_file.write(file_data["content"])
            output_file.write("\n")
    print(f"Data collection complete. Results saved in '{output_file_path}'.")
