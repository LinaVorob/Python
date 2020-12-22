proceeds = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
efficiency = 0

if proceeds > costs:
    efficiency = (proceeds-costs) / proceeds
    num_empl = int(input('Сколько сотрудников в фирме? '))
    eff_empl = (proceeds-costs) / num_empl
    print(f'Фирма работает с прибылью. Рентабельность: {efficiency:.3f}. '
          f'Прибыль в расчете на одного сотрудника: {eff_empl:.3f}')
else:
    print('Фирма работает в убыток')