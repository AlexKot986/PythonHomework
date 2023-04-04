def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ','.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0

    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1

    lastname = format_name(input('Фамилия: '))
    firstname = format_name(input('Имя: '))
    secondname = format_name(input('Отчество: '))
    phone = input('Телефон: ')

    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print('Добавлен ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(new_item[0], new_item[1], new_item[2], new_item[3], new_item[4]))
    data_array.append(new_item)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print('ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[i][0], data_array[i][1], data_array[i][2], data_array[i][3], data_array[i][4]))

def change_item(filename):
    data_array = read_file(filename)
    change_ID = find_item(filename)
    if change_ID != None:
        change_user = input('Изменить? Y/N: ')
        # print(change_ID)
        if change_user.upper() == 'Y':
            what_change = input('Что изменить?\nФамилию - L, Имя - F, Отчество - S, Телефон - P, Всё - любой символ: ')
            if what_change.upper() == 'L':
                data_array[change_ID][1] = format_name(input('Фамилия: '))
            elif what_change.upper() == 'F':
                data_array[change_ID][2] = format_name(input('Имя: '))
            elif what_change.upper() == 'S':
                data_array[change_ID][3] = format_name(input('Отчество: '))
            elif what_change.upper() == 'P':    
                data_array[change_ID][4] = input('Телефон: ')
            else:
                data_array[change_ID][1] = format_name(input('Фамилия: '))
                data_array[change_ID][2] = format_name(input('Имя: '))
                data_array[change_ID][3] = format_name(input('Отчество: '))
                data_array[change_ID][4] = input('Телефон: ')
            print('Изменен ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[change_ID][0], data_array[change_ID][1], data_array[change_ID][2], data_array[change_ID][3], data_array[change_ID][4]))
            
            write_file(filename, data_array)
            return data_array
        else:               
            print('Изменение отменено!')
    

def delete_item(filename):
    data_array = read_file(filename)
    delete_ID = find_item(filename)
    delete_user = input('Удалить? Y/N: ')

    if delete_user.upper() == 'Y':             
        print('Удален ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[delete_ID][0], data_array[delete_ID][1], data_array[delete_ID][2], data_array[delete_ID][3], data_array[delete_ID][4]))
        data_array.pop(delete_ID)
        write_file(filename, data_array)
        return data_array
    else:
        print('Удаление отменено!')


def find_item(filename):
    data_array = read_file(filename)
    find_user = format_name(input('Найти: '))
    count_found_users = {}
    for i in range(1,len(data_array)):
        if find_user in data_array[i]:
            print('Найден ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[i][0], data_array[i][1], data_array[i][2], data_array[i][3], data_array[i][4]))
            found_user = i
            count_found_users[data_array[i][0]] = found_user
            
    # print(count_found_users)
    # print(len(count_found_users))
    if len(count_found_users) > 1:
        print('Выбери ID: ', end='')
        # print(count_found_users[input()])
        try:
            return count_found_users[input()]
        except:
            print('Такого нет! Выбери из найденых!')
    elif len(count_found_users) < 1:
        print('Такого нет!')
    else:
        # print(i, len(data_array) - 1, count_found_users, )
        return found_user

def format_name(name):
    return name[0].upper() + name[1:].lower()

def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    print('5 - Найти запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        change_item(filename)
    elif user_operation == 4:
        delete_item(filename)
    elif user_operation == 5:
        find_item(filename)

filename = 'file.txt'
menu()

