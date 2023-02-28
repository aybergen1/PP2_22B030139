import re

txt = "AasAassl_asAsdsds "
t= re.findall(r"[A-Z][^A-Z]*", txt)
print(t)