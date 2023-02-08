def spy(z):
    for i in range(len(z)-2):
        if z[i] == z[i+1] == 0 and z[i+2] == 7:
            return True
    return False

s=int(input("size of list:"))

w=list()
for i in range(s):
    x=int(input())
    if x == 0 or x == 7:
        w.append(x)
print(spy(w))
