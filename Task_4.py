while True:
    number = input('Введите любое целое положительное число: ')
    if ',' not in number and '.' not in number:
        if int(number) >= 0:
            break

maximum = 0
number = int(number)

while number > 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number // 10

print(f'Самая большая цифра в числе: {maximum}')
