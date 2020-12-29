def sum_non_stop(user_str, need_sum=0):
    user_str = user_str.split()
    if len(user_str) <= 1:
        if user_str != ["Q"]:
            raise TypeError
    if user_str[-1] == "Q":
        user_str.pop()
    for ind in user_str:
        need_sum += float(ind)
    return need_sum


sum_of_numbers = 0
while True:
    try:
        user_str = input('Введите числа через пробел (для завершения работы введите "Q"): ').upper()
        sum_of_numbers = sum_non_stop(user_str, sum_of_numbers)
        print(f'Сумма чисел равна {sum_of_numbers}')
        if "Q" in user_str:
            break
    except TypeError:
        print('Ошибка! Введите числа через пробел или "Q" для выхода')


