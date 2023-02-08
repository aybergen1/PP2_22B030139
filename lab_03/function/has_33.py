
def has_33(e):
    for i in range(len(e)-1):
        if e[i] == e[i+1] == 3:
            return True
    return False
d = int(input("size of lists:"))
e = list()
for i in range(d):
    c = int(input())
    e.append(c)
print(has_33(e))




