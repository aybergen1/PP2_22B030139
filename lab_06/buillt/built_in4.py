import math

p = int(input("same input: \n"))
t = int(input())
print("same output:")
sqr = math.sqrt(p)
import time
time.sleep(t/1000)
print(f"Square root of {p} after {t} miliseconds is {sqr}")
