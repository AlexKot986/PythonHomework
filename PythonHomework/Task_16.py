# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random


while True:
    try:
        N = int(input('Длинна массива: '))
        if N > 0:         
            A = [random.randint(1, 10) for i in range(N)]
            print(A)

            count = 0
            X = int(input('Искомое число: '))
            for i in A:
                if i == X:               
                    count += 1
            if count == 0:
                print(f'Такого числа "{X}" в массиве нет!')
            else:
                print(f'Число {X} встречается {count} раз')

            break
        print('Введите число > 0')
    except:
        print('Это не число!')





