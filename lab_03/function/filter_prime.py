def filter_prime(q):
    for i in range(2,q):
        if q % i == 0:
            return False
        return True
c = int(input("enter size:"))
d = list()
for i in range(c):
    w = int(input())
    if w == 2:
        d.append(w)
    if filter_prime(w):
        d.append(w)
print(d)