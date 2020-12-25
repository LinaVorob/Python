my_list = [7, 5, 3, 3, 2]
while True:
    try:
        user_new_elem = int(input('Введите новое место рейтинга: '))
        break
    except ValueError:
        print("Ошибка! Введите целое число!")
for place in enumerate(my_list):
    if user_new_elem > place[1]:
        my_list.insert(place[0], user_new_elem)
        break
    elif place[0] == len(my_list)-1:
        my_list.append(user_new_elem)
        break
print(my_list)
