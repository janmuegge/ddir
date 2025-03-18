import os
from colorama import Fore, Style, init
import sys

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

def list_dir(extension=None):
    path = "."
    files = os.listdir(path)
    if extension:
            
            files = [f for f in files if f.endswith(extension)]
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

def main():
    args = sys.argv[1:]
    if not args:
        list_dir()
    elif args[0] == "-s" or "-sfe":
        pattern = args[1]
        if pattern.startswith("*."):
            extension = pattern[1:]  
            list_dir(extension)
        else:
            print("Wrong command use 'ddir -help / -?' ")
            
    elif args[0] in ("-help", "-h", "-?"):
        print("""commands: 
              
              search file extention:
              - ddir -s | -sfe *.txt
              
              help menu
              - ddir -h | -help | -?
              
              """)
    else:
        print("Wrong command use 'ddir -help / -?' ")
        
        
        
        
main()