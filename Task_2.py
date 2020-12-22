time_sec = int(input('Введите время в секундах: '))
minute = time_sec//60-(time_sec//3600)*60
print(f'{time_sec//3600:02}:{minute:02}:{time_sec%60:02}')