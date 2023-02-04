# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д

mul = 0
import random
lst = []
new_lst = []
count = 0
for i in range(random.randint(3,10)):
    lst.append(random.randint(0,10))
    count += 1
print(f'Новый список: {lst}')

for i in range(len(lst)):
    while i < len(lst) / 2 and count > len(lst) / 2:
        count -= 1
        mul = lst[i] * lst[count]
        new_lst.append(mul)
        i += 1
print(f'Список произведений пар элементов: {new_lst}')
