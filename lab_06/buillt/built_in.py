from functools import reduce
my_list = [2,3,4,5,6]
product = reduce(lambda x, y: x * y, my_list)
print(product)