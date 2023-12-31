# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

# Вариант 1: 

coins = int(input('Введите количество монеток, которые лежат на столе \n'))

amount = []
for i in range (0, coins):
    amount.append(randint(0,1))
print(amount)

heads = 0
tiles = 0

for i in amount:
    if i == 0: 
        tiles +=1
    else: 
        heads +=1

print(heads, tiles)

if heads == 0 or tiles == 0: print('все монетки лежат одной стороной, ничего не надо переворачивать')
elif heads > tiles: print(f'Чтоб все монетки лежали одной стороной надо повернуть {tiles} из них')
else: print(f'Чтоб все монетки лежали одной стороной надо повернуть {heads} из них')

# ___________________________________________________________________
# Вариант 2: 

# coins = int(input('Введите количество монеток, которые лежат на столе \n'))
# heads = randint(1, coins-1)
# tails = coins - heads

# turner = 0

# if heads > tails: turner = tails
# else: turner = heads  

# print (f'Итак. У нас {coins} монет, из которых, {heads} - орлом, а {tails} - решкой (так решил святой рандом). \nА чтоб все монеты лежали одной стороной, минимум надо повернуть {turner}')