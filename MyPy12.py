# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

import random
lst_float = []

for i in range(random.randint(3,10)):
    lst_float.append(round(random.uniform(0, 100), 2))
print(f'Новый список вещественных чисел: {lst_float}')

new_lst_float = [round(i % 1, 2) for i in lst_float]
print(f'Список дробных частей: {new_lst_float}')

print(f'Разница между макс. и мин. значением дробной части элементов: {round(max(new_lst_float) - min(new_lst_float), 2)}')