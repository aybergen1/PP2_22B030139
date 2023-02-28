import re

tst = input()
r = re.findall("ab{2,3}",tst)
print(r)