# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
while 1:
    try:
        numbers_n = [random.randint(0, 20) for i in range(int(input('n: ')))]
        numbers_m = [random.randint(0, 20) for i in range(int(input('m: ')))]

        if len(set(numbers_n).intersection(set(numbers_m))) == 0 or len(numbers_n) == 0 or len(numbers_m) == 0:
            print(numbers_n)
            print(numbers_m)
            print('Неа!!!')
            break
        else:
            print(numbers_n)
            print(numbers_m)
            print('->', sorted(set(numbers_n).intersection(set(numbers_m))))
            break
        
    except:
        print('Ещё!!!')