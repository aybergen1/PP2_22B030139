import re

tst = "asb assl assdsds "
r = re.findall(r"a.*b",tst)
print(r)
