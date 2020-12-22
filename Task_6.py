km = int(input('Введите результат пробежки на 1-ый день в км: '))
needed_km = int(input('Введите нужную дистанцию в км: '))
step = 1
while True:
    km += km * 0.1
    step += 1
    if km >= needed_km:
        print(f'На {step}-й день спортсмен достиг результата - не менее {needed_km} км.')
        break
