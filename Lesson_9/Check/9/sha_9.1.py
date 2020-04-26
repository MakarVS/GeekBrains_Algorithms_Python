# Определение количества различных подстрок с использованием хеш-функции. 
# Пусть на вход функции дана строка. 
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# в сумму не включаем пустую строку и строку целиком;
# без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
from hashlib import sha1

string = input('Введите строку: ')

str_len = len(string)
sub_len = 1

sub_strings = []

while str_len > 1:
    for i in range(str_len):
        sub = sha1(string[i:i + sub_len].encode('utf-8')).hexdigest()
        if sub not in sub_strings:
            sub_strings.append(sub)
    sub_len += 1
    str_len -= 1

print(f'В строке "{string}" {len(sub_strings)} уникальных подстрок')