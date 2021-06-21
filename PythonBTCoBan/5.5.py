import os
print("Nhap duong dan:")
path = str(input())

for i in os.scandir(path):
    if i.is_dir():
        print('Folder: ' + i.path)
