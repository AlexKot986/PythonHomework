# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8


while 1:
    try:
        N = int(input('Введите число: '))
        if N > 0:
            break
        print('Введите число > 0!')
    except:
        print('Некорректный ввод!')

print(N, '->', *[3 ** i for i in range(N + 1) if 3 ** i <= N])
