import math

def degrees_to_radians(degrees):
    degree = int(input("Input degree: "))
    radians = degrees * math.pi / 180
    return radians

def trapezoidArea():
    h = int(input("Height: "))
    a = int(input("Base, first value: "))
    b = int(input("Base, second value: "))
    area = ((a + b) / 2) * h
    return area

def polygonArea():
    n = int(input("Input number of sides: "))
    length = int(input("Input the length of sides: "))
    area = (n * (length**2)) / (4 * math.tan(math.pi/n))
    return area

def parallelogramArea():
    length = int(input("Length of base: "))
    height = int(input("Height of parallelogram: "))
    area = float(length * height)
    return area