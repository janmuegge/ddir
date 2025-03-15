import os

FILE_ICONS = {
    ".py": "",
    ".txt": "",
    ".json": "", 
    "dir": "",  
}

def list_dir():
    path = "." 
    files = os.listdir(path)

    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            icon = FILE_ICONS["dir"]
        else:
            ext = os.path.splitext(file)[1]
            icon = FILE_ICONS.get(ext, "")  
        
        print(f"{icon}  {file}")

if __name__ == "__main__":
    list_dir()
