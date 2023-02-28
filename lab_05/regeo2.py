import re

tst = "ab_cd rtey r_w"
r = re.findall(r"\b[a-z]+_[a-z]+\b",tst)
print(r)