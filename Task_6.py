from itertools import count, cycle

work_numbers = input("Введите число начала работы итератора и число остановки: ").split()

for el in count(int(work_numbers[0])):
    if el == int(work_numbers[1]):
        print(el)
        break
    else:
        print(el, end=", ")

cycle_list = [1, 5, 2, 9, 123, 654, 234, 987, 1212, 54]
for id, el in enumerate(cycle(cycle_list)):
    if id == len(cycle_list) - 1:
        print(el)
        break
    else:
        print(el, end=', ')
