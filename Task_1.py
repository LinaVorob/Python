def division_numbers(numerator, denominator):
    return numerator / denominator


while True:
    try:
        number_1 = float(input("Введите числитель: ").replace(',', '.'))
        number_2 = float(input("Введите знаменатель: ").replace(',', '.'))
        print(f'{number_1} / {number_2} = {division_numbers(number_1, number_2):.3f}')
        break
    except ValueError:
        print('Ошибка! Нужно вводить числа! Попробуйте еще раз.')
    except ZeroDivisionError:
        print('Ошибка! Деление на ноль! Попробуйте еще раз.')
