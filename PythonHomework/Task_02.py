# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

while 1:
    number = input('Введите число: ')
    
    if number.isdigit() == True: 
        sum = 0
        for i in number:
            sum += int(i)
        print('Сумма цифр числа', number, '->', sum)
        break 

    else:
        print('Это не число!!!')

