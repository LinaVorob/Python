user_list = input('Введите значения списка через пробел: ').split()
for id, item in enumerate(user_list):
    if id % 2 == 1:
        user_list[id] = user_list[id-1]
        user_list[id-1] = item
print(user_list)
