# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint as r

print(lst := [r(1,10) for _ in range(10)])
min = int(input('задайте минимальное значение диапазона: '))
max = int(input('задайте максимальное значение диапазона: '))

print(ind := [i for i in range(len(lst)) if min <= lst[i] <= max])
