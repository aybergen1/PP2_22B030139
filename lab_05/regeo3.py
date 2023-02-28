import re

tst = "Ab_cd Wey rDw"
r = re.findall(r"[A-Z][a-z]+",tst)
print(r)
