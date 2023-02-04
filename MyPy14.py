# Негафибоначчи

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
count = int(input('Введите количество элементов последовательности: '))

for f in range(1, count + 1):
    list.append(Fibonacci(f))
    list.insert(0, NegaFibonacci(f))
print(list)

# Вариант выполнения задания не до конца реализован
# def NegaFibonacci(n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n < 0:
#             return ((-1)**(-n + 1)) * NegaFibonacci(-n)
#         return NegaFibonacci(n - 1)+NegaFibonacci(n - 2)

# count = int(input('Введите количество элементов последовательности: '))

# for f in range(count):
#     print(NegaFibonacci(f), end = " ")