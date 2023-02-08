import math
def volume(radius):
    v=(4/3)*(radius**3)*math.pi
    return v
radius=int(input("radius of sphere:"))
print(volume(radius))
