import re

tst = "asb assl as,sdsds "
r = re.sub("\s", ":", tst)
r = re.sub("[.]", ":", r)
r = re.sub(",", ":", r)
print(r)
