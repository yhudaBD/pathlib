from pathlib import Path

file_path = Path('notes.txt')

if file_path.exists():
    print('File exists')
else:
    file_path.write_text('This is a new file created by pathlib')

print(file_path.read_text())