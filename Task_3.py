with open('Employers.txt', encoding='utf-8') as f:
    sum_of_rate = []
    print('Фамилии сотрудников, у кого оклад менее 20 000 руб.:')
    for empl in f.readlines():
        empl = empl.split()
        sum_of_rate.append(float(empl[1]))
        if float(empl[1]) < 20000:
            print(empl[0])
    print(f'Средняя величина дохода сотрудников: {sum(sum_of_rate)/len(sum_of_rate)}')