import sys

try:
    if 'h' in sys.argv[1:]:
        print('Введите через пробел выработку сотрудника в часах, его ставку в час и начисляемую премию')
    else:
        all_work, rate, prize = sys.argv[1:]
        print(f'Заработная плата сотрудника: {float(all_work) * float(rate) + float(prize)}')
except ValueError:
    print("Введите 3 числа подряд через запятую (выработку сотрудника в ч., его ставку в ч., премия)")
