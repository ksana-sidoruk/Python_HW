# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = 5 # int(input('Введите сумму загаданных чисел: '))
multip = 6 #int(input('Введите произведение загаданных чисел: '))

for x in range(1, sum):
    for y in range(1, sum):
        if x + y == sum and x * y == multip:
            print(f'Либо брат загадал x = {x} и y = {y}')
            break

