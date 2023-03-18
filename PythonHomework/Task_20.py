# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12


def ScrabbleLatin(word):
    dictionary_Latin = {}
    latin = [chr(i) for i in range(65, 91)]
    for i in range(len(latin)):
        if latin[i] == 'Q' or latin[i] == 'Z':
            dictionary_Latin[latin[i]] = 10
        elif latin[i] == 'J' or latin[i] == 'X':
            dictionary_Latin[latin[i]] = 8
        elif latin[i] == 'K':
            dictionary_Latin[latin[i]] = 5
        elif latin[i] == 'F' or latin[i] == 'H' or latin[i] == 'V'or latin[i] == 'W'or latin[i] == 'Y':
            dictionary_Latin[latin[i]] = 4
        elif latin[i] == 'B' or latin[i] == 'C'or latin[i] == 'M' or latin[i] == 'P':
            dictionary_Latin[latin[i]] = 3
        elif latin[i] == 'D' or latin[i] == 'G':
            dictionary_Latin[latin[i]] = 2
        else:
            dictionary_Latin[latin[i]] = 1
              
    count = 0
    for i in word.upper():
        count = count + int(dictionary_Latin[i])
    return count

def ScrabbleKiril(word):
    dictionary_Kiril = {}
    kiril = [chr(i) for i in range(1040, 1072)]
    for i in range(len(kiril)):
        if kiril[i] == 'Ф' or kiril[i] == 'Щ' or kiril[i] == 'Ъ':
            dictionary_Kiril[kiril[i]] = 10
        elif kiril[i] == 'Ш' or kiril[i] == 'Э' or kiril[i] == 'Ю':
            dictionary_Kiril[kiril[i]] = 8
        elif kiril[i] == 'Ж' or kiril[i] == 'З'or kiril[i] == 'Х'or kiril[i] == 'Ц'or kiril[i] == 'Ч':
            dictionary_Kiril[kiril[i]] = 5
        elif kiril[i] == 'Й' or kiril[i] == 'Ы':
            dictionary_Kiril[kiril[i]] = 4
        elif kiril[i] == 'Б' or kiril[i] == 'Г'or kiril[i] == 'Ё' or kiril[i] == 'Ь' or kiril[i] == 'Я':
            dictionary_Kiril[kiril[i]] = 3
        elif kiril[i] == 'Д' or kiril[i] == 'К' or kiril[i] == 'Л'or kiril[i] == 'М'or kiril[i] == 'П'or kiril[i] == 'У':
            dictionary_Kiril[kiril[i]] = 2
        else:
            dictionary_Kiril[kiril[i]] = 1

    count = 0
    for i in word.upper():
        count = count + int(dictionary_Kiril[i])
    return count

def LatinOrKiril(word):
    latin_word = 0
    kiril_word = 0

    for i in word.upper():
        if ord(i) >= 65 and ord(i) < 91:
            latin_word += 1
        if ord(i) >= 1040 and ord(i) < 1072:
            kiril_word += 1
    if len(word) == latin_word:
        return 0
    elif len(word) == kiril_word:
        return 1
    else:
        return 2

while True:
    try:   
        word = str(input('Введите слово: '))
        if len(word) > 0:
            if LatinOrKiril(word) == 0:
                print('Слово', word, '=', ScrabbleLatin(word), 'очков')
                break
            elif LatinOrKiril(word) == 1:
                print('Слово', word, '=', ScrabbleKiril(word), 'очков')
                break
            else:
                print('Странное слово, попробуйте другое!')
        else:
            print('В слове должна быть хоть одна буква!')
    except:
        print('Что-то пошло не так, попробуйте еще!')
                        

    