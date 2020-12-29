def user_data(name, surname, **kwargs):
    data_of_user = f'name: {name}, surname: {surname}'
    if len(kwargs) != 0:
        for key in kwargs.keys():
            data_of_user += f', {key}: {kwargs[key]}'
    return data_of_user


user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_year = int(input('Введите год рождения: '))
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_phone = input('Введите номер телефона: ')

print(user_data(surname=user_surname, year=user_year, name=user_name, phone=user_phone, city=user_city,
                email=user_email))
