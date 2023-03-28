# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Ввод: min = 7, max = 10
# Вывод: [1, 9, 13, 14, 19]

import random

arr = [random.randint(1, 20) for _ in range(random.randint(10, 20))]

def GetIndx(array, min, max):
    result = []
    for i in range(len(array)):
        if array[i] >= min and array[i] <= max:
            result.append(i)
    return result

mi, ma = random.randint(1, 10),random.randint(10, 20)

print(arr)
print(f'min = {mi}, max = {ma}\n{GetIndx(arr, mi, ma)}')