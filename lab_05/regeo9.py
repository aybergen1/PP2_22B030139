import re
txt = input()
x = re.sub(r"([A-Z][a-z]+)", r" \1", txt).strip()
x = x.split(' ')
s = ''
for i in range(0, len(x)):
    s += x[i].lower() + '_'
print(s[:-1])