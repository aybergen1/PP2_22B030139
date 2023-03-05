import os
path = r"C:\Users\ASUS\Desktop\qwse\lab_06\qwe\W.txt"
if os.access(path,os.F_OK):
    os.remove(path)
else:
    print("do not  exist!")
