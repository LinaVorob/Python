user_string = input("Введите любые слова через пробел: ").split(" ")
for word in enumerate(user_string):
    print(f'{word[0]}. {word[1][:10]}')

