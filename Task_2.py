# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.

#  Пример:

#  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def create_sequence(number: int):
    seq = [1]
    for i in range(1, number):
        seq.append(seq[i-1]*(i+1))
    return seq

numb = int(input('Enter your number: '))
print(create_sequence(numb))
