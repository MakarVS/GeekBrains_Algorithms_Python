# Задача № 3.
# Написать программу, которая генерирует в указанных пользователем границах:
#   a. случайное целое число,
#   b. случайное вещественное число,
#   c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
import re

bord_1 = input('Введите первую границу диапазона: ')
cond_left_board = True

# Реализовал обработку любого пользовательского ввода. Знаю, что не обязательно, было интересно для себя.
try:
    buf = float(bord_1)
    if bord_1.isnumeric():
        bord_1 = int(bord_1)
    else:
        bord_1 = buf
except ValueError:
    if not(len(bord_1) == 1 and re.match(r'[a-zA-Z]', bord_1)):
        cond_left_board = False
        print('Первая граница не является одиночной латинской буквой!')

if cond_left_board:
    bord_2 = input('Введите вторую границу диапазона: ')
    cond_right_board = True

    try:
        buf = float(bord_2)
        if bord_2.isnumeric():
            bord_2 = int(bord_2)
        else:
            bord_2 = buf
    except ValueError:
        if not (len(bord_2) == 1 and re.match(r'[a-zA-Z]', bord_2)):
            cond_right_board = False
            print('Вторая граница не является одиночной латинской буквой!')

if cond_left_board and cond_right_board:
    bord_type_1 = type(bord_1)
    bord_type_2 = type(bord_2)
    if bord_type_1 == bord_type_2:
        bord_1, bord_2 = min(bord_1, bord_2), max(bord_1, bord_2)
        if bord_type_1 == int:
            print(f'Случайное целое число из диапазона {bord_1} - {bord_2} равно {random.randint(bord_1, bord_2)}')
        elif bord_type_1 == float:
            print(f'Случайное вещественное число из диапазона {bord_1} - {bord_2} равно '
                  f'{random.uniform(bord_1, bord_2)}')
        else:
            print(f'Случайный символ латинского алфавита из диапазона {bord_1} - {bord_2} равен '
                  f'{chr(random.randint(ord(bord_1.lower()), ord(bord_2.lower())))}')
    else:
        print('Типы диапазонов разные!')
