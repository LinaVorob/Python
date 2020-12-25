seasons = ["зима", "весна", "лето", "осень"]
while True:
    try:
        number_of_month = int(input('Введите номер интересующего месяца: '))
        if number_of_month <= 0 or number_of_month > 12:
            raise OverflowError
        break
    except ValueError:
        print('Ошибка! необходимо ввести число месяца!')
    except OverflowError:
        print('Ошибка! Такого месяца не существует! Введите число от 1 до 12')
print(f'Месяц относится к времени года: {seasons[0 if number_of_month == 12 else number_of_month//3]}')

