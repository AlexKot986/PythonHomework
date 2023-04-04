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
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
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
    change_user = input('Изменить? Y/N: ')
    
    if change_user.upper() == 'Y':
        lastname = input('Фамилия: ')
        firstname = input('Имя: ')
        secondname = input('Отчество: ')
        phone = input('Телефон: ')
        data_array[change_ID][1] = lastname
        data_array[change_ID][2] = firstname
        data_array[change_ID][3] = secondname
        data_array[change_ID][4] = phone
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
    find_user = input('Найти: ')
    for i in range(1,len(data_array)):
        if find_user in data_array[i]:
            print('Найден ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[i][0], data_array[i][1], data_array[i][2], data_array[i][3], data_array[i][4]))
            return i
    print('Такого нет!')



def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        change_item(filename)
    elif user_operation == 4:
        delete_item(filename)
    # elif user_operation == 5:
    #     find_item(filename)

filename = 'file.txt'
menu()

