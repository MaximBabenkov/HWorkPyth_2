# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях

def fill_list(value: int):
    from random import randint
    a = []
    for i in range(value):
        a.append(randint(-value, value))
    return a

def remove_space(row: str):
    digits = []
    for i in range(len(row)):
        if row[i] != ' ':
            digits.append(int(row[i]))
    return digits

def mult_items(numbs: list, indexes: list):
    ind_1 = indexes[0]
    ind_2 = indexes[1]
    product = numbs[ind_1]*numbs[ind_2]
    return product

size = int(input('Enter your size of a list: '))
list_numbers = fill_list(size)
print('Your list of numbers:', list_numbers)
indexes_in_str= input('Enter two space-separated indexes of items to multiply: ')
indexes_to_mult= remove_space(indexes_in_str)
result = mult_items(list_numbers, indexes_to_mult)
print('Product:', result)
