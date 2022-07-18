#  Задайте список из n чисел последовательности 
#  (1+1/n)^n и выведите на экран их сумму.

def create_sequence(number: int):
    seq = []
    for number in range(1, number+1):
        item = round(((1+1/number)**number), 3)
        seq.append(item)
    return seq

def find_summ(digits: list):
    summ = 0
    for i in range(len(digits)):
        summ = digits[i] + summ
    return summ

numb = int(input('Enter your number: '))
sequence = create_sequence(numb)
print('Your sequence: ', sequence)
summ = find_summ(sequence)
print('Sum of numbers: ', round(summ, 3))
