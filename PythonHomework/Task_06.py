# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

def IsDig(number):
    while 1:        
        if number.isdigit() == True and len(number) == 6:
            return number
        else:
            print('Это не то!')
            number = input('Введите шестизначное число: ')

def sum(number):
    s = 0
    for i in number:
        s += int(i)
    return s


ticket_number = IsDig(input('Шестизначный номер билета: '))

if sum(ticket_number[:3]) == sum(ticket_number[len(ticket_number) - 3:]):
    print(ticket_number, '->', 'Yes')
else:
    print(ticket_number, '->', 'No')