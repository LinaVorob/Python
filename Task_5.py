with open('sum_of_numbers.txt') as f:
    try:
        print(sum(map(float, f.read().split())))
    except ValueError:
        print('Ошибка! В файле есть нечисловые значения')
