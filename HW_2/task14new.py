# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите ваше число N \n'))

list_2k = []
j = 0

for i in range(0, number+1):
    if i == 2**j:
        list_2k.append(i)
        j += 1

print(*list_2k)
