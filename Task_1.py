#  Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

#  Пример:

# - 6782 -> 23
# - 0,56 -> 11

def remove_comma(number: str):
    numerals = []
    for i in range(len(number)):
        if number[i] != '.':
            numerals.append(int(number[i]))
    return numerals

def find_summ(digits: list):
    summ = 0
    for i in range(len(digits)):
        summ += digits[i]
    return summ

numb = input('Enter your number: ')
dig = remove_comma(numb)
print('The sum of digits of this number:', find_summ(dig))

