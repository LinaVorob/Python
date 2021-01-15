with open('homework_two.txt', encoding='utf-8') as f:
    print(f'Количество строк в файле: {len(f.readlines())}.')
    f.seek(0)
    for ids, el in enumerate(f.readlines()):
        print(f'В {ids + 1}-й строке количество слов равно {len(el.split())}.')
