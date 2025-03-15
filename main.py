import os
from colorama import Fore, Style, init

FILE_ICONS = {
    ".py": "",
    ".js": "",
    ".ts": "",
    ".html": "",
    ".css": "",
    ".php": "",
    ".c": "",
    ".cpp": "",
    ".java": "",
    ".rs": "",
    ".go": "",
    ".sh": "",
    ".bat": "",

    ".json": "",
    ".yaml": "",
    ".yml": "",
    ".toml": "",
    ".xml": "謹",
    ".csv": "",
    ".sql": "",

    ".txt": "",
    ".md": "",
    ".pdf": "",
    ".doc": "",
    ".docx": "",
    ".ppt": "",
    ".pptx": "",
    ".xls": "",
    ".xlsx": "",

    ".png": "",
    ".jpg": "",
    ".jpeg": "",
    ".gif": "",
    ".svg": "",
    ".mp4": "",
    ".mkv": "",
    ".mp3": "",
    ".wav": "",

    ".zip": "",
    ".tar": "",
    ".gz": "",
    ".rar": "",
    ".7z": "",

    ".exe": "",
    ".dll": "",
    ".iso": "",
    ".log": "",
    ".config": "",

    "dir": "",
    "default": ""
}

def list_dir():
    path = "."
    files = os.listdir(path)

    if not files:
        print("[No files found]")
        return

    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            icon = FILE_ICONS["dir"]
        else:
            ext = os.path.splitext(file)[1]
            icon = FILE_ICONS.get(ext, "")

        count_files = len(files)
        print(f"{icon}  {file}")
    print("---")
    print("Found {} files".format(count_files))

list_dir()

