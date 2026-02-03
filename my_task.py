from pathlib import Path

current_dir = Path.cwd()
print(current_dir)

file_path = current_dir / 'files' / 'data.txt'

print(file_path.parent)

home_dir = Path.home()
print(home_dir)