def my_func(val_1, val_2, val_3):
    """
    Function returns the sum of the two largest numbers
    :param val_1: Any number or string
    :param val_2: Any number or string
    :param val_3: Any number or string
    """
    try:
        return val_2 + val_3 + val_1 - min(val_1, val_2, val_3)
    except TypeError:
        minimum = list(filter(min, [str(val_1), str(val_2), str(val_3)]))
        return minimum[0]+minimum[1]

print(my_func(7, 5, 23.3))
