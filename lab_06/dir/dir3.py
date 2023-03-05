import os
path = r'/lab_06/qqqqq.txt'
if os.access(path, os.F_OK):
     print(os.path.basename(path))
     print(os.path.dirname(path))
else:
     print(f"{path} do not exists")