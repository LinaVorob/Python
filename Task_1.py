with open('homework_one.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст: ')
        if line == '':
            break
        f.write(f'{line}\n')

