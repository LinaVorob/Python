def my_func(x, y):
    if x <= 0 or y >= 0 or -y % 1 != 0:
        raise TypeError
    degree = x
    for step in range(-y - 1):
        degree *= x
    return 1 / degree


while True:
    try:
        user_X = float(input("Введите значение Х: ").replace(",", "."))
        user_Y = int(input("Введите значение Y: "))
        if user_Y >= 0:
            user_Y = -user_Y
        print(my_func(user_X, user_Y))
        break
    except ValueError:
        print("Ошибка! Необходимо ввести числа! Y должен быть целым и меньше нуля")
