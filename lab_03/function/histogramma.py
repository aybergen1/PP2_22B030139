def histo(f):
   return "*"*f
f=int(input("size of list:"))
d=list()
for i in range(f):
    r=int(input())
    d.append(r)
for i in range(len(d)):
    print(histo(d[i]))

