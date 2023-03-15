# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

while 1:
    try:
        number = int(input("Введите число монет: "))
        if number != 0:
            break
        else:
            print("Нет монет!")
    except:
        print("Некорректный ввод. Попробуйте еще раз!")

    
monets = [random.randint(0, 1) for i in range(number)]
print(monets)

head_count = 0
tail_count = 0

for e in monets:
    if e == 0:
        head_count += 1
    if e == 1:
        tail_count += 1

def pr(ht):    
    if ht == 0:
        print(f"Переверните {head_count} Heads")
    if ht == 1:
        print(f"Переверните {tail_count} Tails")


if head_count == 0 or tail_count == 0:
    print("Ничего переворачивать не надо!")
elif head_count < tail_count:
    pr(0)
elif head_count > tail_count:
    pr(1)
elif head_count == tail_count:
    pr(random.randint(0, 1))
   
