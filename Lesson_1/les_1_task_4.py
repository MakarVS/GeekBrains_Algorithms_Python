# Задача № 4.
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import re

letter_1 = input('Введите первую букву: ')

if len(letter_1) == 1 and re.match(r'[a-zA-Z]', letter_1):
    letter_2 = input('Введите вторую букву: ')
    if len(letter_2) == 1 and re.match(r'[a-zA-Z]', letter_2):
        letter_1 = letter_1.lower()
        letter_2 = letter_2.lower()
        letter_1, letter_2 = min(letter_1, letter_2), max(letter_1, letter_2)
        ucd_letter_1 = ord(letter_1)
        ucd_letter_2 = ord(letter_2)
        print(f'Порядковый номер буквы "{letter_1}" в латинском алфавите: {ucd_letter_1 - 96}')
        print(f'Порядковый номер буквы "{letter_2}" в латинском алфавите: {ucd_letter_2 - 96}')
        print(f'Кол-во букв между "{letter_1}" и "{letter_2}" '
              f'равно {ucd_letter_2 - ucd_letter_1 - 1}')
    else:
        print('Это не одиночная буква латинского алфавита!')
else:
    print('Это не одиночная буква латинского алфавита!')
