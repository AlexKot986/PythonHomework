# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

while True:
    try:
        N = int(input('Длинна массива: '))
        if N > 0:         
            A = [random.randint(0, 10) for i in range(N)]
            print(A)
          
            X = int(input('Число: '))
            indx = 0
            for i in A:
                if A[indx] == X:
                    indx += 1
                else:
                    result = A[indx]
                    break
            if indx >= len(A):
                print(f'Массив содержит только "{X}" элементы!')
            else: 
                for i in A:
                    if i != X and abs(X - i) <= abs(X - result):
                        if abs(X - i) == abs(X - result) and i > result:
                            continue
                        else:
                            result = i
           
                print(f'Близкое по значению к числу {X} в массиве это {result}')

            break
        print('Введите число > 0')
    except:
        print('Это не число!')
