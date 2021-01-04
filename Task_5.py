from functools import reduce

even_number = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(lambda x, y: x * y, even_number))
