# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
import random
list_rand = []
summ = 0
for i in range(random.randint(3,10)):
    list_rand.append(random.randint(0,10))
print(f'Новый список: {list_rand}')

for i in range(len(list_rand)):
    if i % 2 != 0:
        summ += list_rand[i]

print(f'Сумма нечетных элементов списка: {summ}')