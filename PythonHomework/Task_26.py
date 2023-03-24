# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

import random

A = random.randint(1, 10)
B = random.randint(1, 10)
print(f'A = {A}, B = {B}')

def NumPow(n, m):
    if m == 0:
        return 1
    
    return n * NumPow(n, m - 1)

print(f'A ^ B = {NumPow(A, B)}')