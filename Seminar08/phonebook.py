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
    # print(next_id)
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
    # print(data_array)
    data_array.append(new_item)
    # print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        # print("ID:", data_array[i][0], "Фамилия:", data_array[i][1],"Имя:", data_array[i][2], "Отчество:", data_array[i][3], "Телефон:", data_array[i][4])
        print('ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[i][0], data_array[i][1], data_array[i][2], data_array[i][3], data_array[i][4]))

def change_item(filename):
    data_array = read_file(filename)
    change_ID = input('Введите ID: ')
    for i in range(1,len(data_array)):
        if change_ID == data_array[i][0]:
            lastname = input('Фамилия: ')
            firstname = input('Имя: ')
            secondname = input('Отчество: ')
            phone = input('Телефон: ')
            data_array[i][1] = lastname
            data_array[i][2] = firstname
            data_array[i][3] = secondname
            data_array[i][4] = phone
            print('Изменен ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[i][0], data_array[i][1], data_array[i][2], data_array[i][3], data_array[i][4]))
            # print(data_array)
            # data_array.append(new_item)
            # print(data_array)
            write_file(filename, data_array)
            return data_array
        
    print('Такого ID нет!')
    

def delete_item(filename):
    data_array = read_file(filename)
    delete_ID = input('Введите ID: ')
    for i in range(1,len(data_array)):
        if delete_ID == data_array[i][0]:           
            print('Удален ID: {}  Фамилия: {}  Имя: {}  Отчество: {}  Телефон: {}'.format(data_array[i][0], data_array[i][1], data_array[i][2], data_array[i][3], data_array[i][4]))
            data_array.pop(i)
            write_file(filename, data_array)
            return data_array
    print('Такого ID нет!')



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

filename = 'file.txt'
menu()

