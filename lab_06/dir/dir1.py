import os
path  = os.getcwd()
files =os.listdir(path)
print(files)
for file in files:
    if os.path.isdir(file):
        print(file)

for file in files:
    if os.path.isfile(file):
        print(file)
