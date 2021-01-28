from itertools import count


def fact(n):
    res = 1
    for id, el in enumerate(count(1)):
        res *= el
        yield res
        if id == n - 1:
            break


number = int(input("Введите число: "))
for el in fact(number):
    print(el)
