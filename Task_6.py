list_of_product = []
id_product = 0
while True:
    product = input("Введите название товара, цену, количество и ед. измерения (через проблел): ").split(' ')
    product_dict = {'название': product[0], 'цена': product[1], 'количество': product[2], 'ед.': product[3]}
    id_product += 1
    list_of_product.append((id_product, product_dict))
    closing = input("Завершить ввод? (ДА - для завершения) ").lower()
    if closing == "да":
        break
analyz = {'название': [list_of_product[0][1]['название']], 'цена': [list_of_product[0][1]['цена']],
          'количество': [list_of_product[0][1]['количество']], 'ед.': [list_of_product[0][1]['ед.']]}
for id, el in enumerate(list_of_product):
    if id == 0:
        continue
    for key in list_of_product[id][1].keys():
        interval_list = analyz[key]
        interval_list += [list_of_product[id][1][key]]
        analyz[key] = interval_list
print(list_of_product)
print(analyz)
