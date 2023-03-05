import os
path = r"/lab_06/qwe"
for i in range(65, 91):
    name = os.path.join(path, chr(i) +".txt")
    f = open(name, "a")