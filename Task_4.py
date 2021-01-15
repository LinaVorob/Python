number_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть",
               "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
with open('Translate_numbers.txt', encoding='utf-8') as f:
    numbers = f.readlines()
with open('new_numbers.txt', 'w', encoding='utf-8') as file:
    for el in numbers:
        el = el.split(' ', 1)
        file.write(f'{number_dict[el[0]]} {el[1]}')
