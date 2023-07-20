# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

from math import sqrt


number = int(input('Введите ваше число N \n'))

list_2k = []

for i in range(0, number+1):
    for j in range (0, number):
        if i == 2**j:
            list_2k.append(i)
            break


print(*list_2k)
