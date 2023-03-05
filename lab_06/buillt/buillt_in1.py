p="qawsedrftyguSXRDCFTVGBHNJ"
u = 0
l = 0
for i in p:
    if i.isupper():
        u += 1
    if i.islower():
        l+=1
print(f"upper:{u} \nlower:{l}")