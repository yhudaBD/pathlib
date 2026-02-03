from pathlib import Path

path = Path.cwd()
files_count = 0
folders_count = 0

for item in path.iterdir():
    if item.is_dir():
        print("Folder:", item.name)
        folders_count += 1
    elif item.is_file():
        print("File:", item.name)
        files_count += 1
print("Folders count:", folders_count)
print("Files count:", files_count)