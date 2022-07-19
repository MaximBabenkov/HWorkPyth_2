# Реализуйте алгоритм перемешивания списка

def fill_list(size: int, min_value: int, max_value: int):
    from random import randint
    list = []
    for i in range(size):
        list.append(randint(min_value, max_value))
    return list

def list_mixer(list: list):
    from random import randint
    for i in range(len(list)):
        i_change = randint(0,len(list)-1)
        list[i], list[i_change] = list[i_change], list[i]
    return list


amount = int(input('Enter amount of items in your list: '))
minn = int(input('Enter the minimum value in your list: '))
maxx = int(input('Enter the maximum value in your list: '))
list_in = fill_list(amount, minn, maxx)
print('Your list:')
print(list_in)
list_out = list_mixer(list_in)
print('Your mixed list:')
print(list_out)
