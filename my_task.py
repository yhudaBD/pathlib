from pathlib import Path


path = Path('documents/reports/annual_report.pdf')

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

for p in path.parents:
    print(p)

