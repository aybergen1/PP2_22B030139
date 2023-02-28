import re

txt = "AasAassl_asAsdsds "
x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
print(x)