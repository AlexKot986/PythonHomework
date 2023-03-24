# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

import random

a = random.randint(1, 10)
b = random.randint(1, 10)
print(f'a = {a}, b = {b}')

def NumSum(n, m):
    if m == 0:
        return n
    n += 1
    return NumSum(n, m - 1)

print(f'a + b = {NumSum(a, b)}')

