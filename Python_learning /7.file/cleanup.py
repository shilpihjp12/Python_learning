import os

folder = './Users/spriya/Python_learning/7.file'

entries = os.scandir(folder)

for entry in entries:
    if os.path.is_file():
      print(entry.name)
        