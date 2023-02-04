# Напишите программу, которая будет преобразовывать десятичное число в двоичное

number = int(input('Введите целое число: '))
start_num = number
bin_number = ""
while number != 0:
    bin_number = str(number % 2) + bin_number
    number //= 2
print(f'Число {start_num} в десятичной => {bin_number} в двоичной')