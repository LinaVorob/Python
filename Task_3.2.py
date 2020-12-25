seasons = {"зима": (12, 1, 2), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
while True:
    try:
        number_of_month = int(input('Введите номер интересующего месяца :'))
        if number_of_month <= 0 or number_of_month > 12:
            raise OverflowError
        break
    except ValueError:
        print('Ошибка! необходимо ввести число месяца!')
    except OverflowError:
        print('Ошибка! Такого месяца не существует! Введите число от 1 до 12')
for elem in seasons.keys():
    if number_of_month in seasons[elem]:
        print(f'Месяц относится к времени года: {elem}')
        break
