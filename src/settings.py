import os
from typing import List
from pydantic_settings import BaseSettings


ENV_FILE=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")


class Settings(BaseSettings):
    project_path: str = "/home/legion/gitlab/parsers/api"  # source path
    output_file_path: str = "/home/legion/Downloads/project_code.txt"  # dest path
    extensions: list = [".py"]
    exclude_dirs: List[str] = ["venv", "__pycache__"]
    exclude_files: List[str] = ["proxy_checker.py"]
    include_files: List[str] = ["Dockerfile"]

    class Config:
        env_file = ENV_FILE
        env_file_encoding = "utf-8"


def load_settings() -> Settings:
    """Force reload of settings from the .env file."""

    env_variables = {
        key
        for key in os.environ.keys()
        if key.startswith(Settings.model_config["env_prefix"])
    }
    for variable in env_variables:
        os.environ.pop(variable, None)
    return Settings(_env_file=ENV_FILE)
