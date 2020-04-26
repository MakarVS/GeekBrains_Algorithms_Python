'''
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления
хеша (hash(), sha1() или любая другая из модуля hashlib)
'''

import hashlib

def ft_substr_qty(str):
    res = []
    h_str = hashlib.sha1(str.encode('utf-8')).hexdigest()
    for i in range(len(str) + 1):
        for j in range(i + 1, len(str) + 1):
            h_sub = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
            if (h_sub not in res) and (h_sub != h_str):
                res.append(h_sub)
    return len(res)

str = input("Put string for parsing: ")
while (len(str) == 0):
    print("Please, put any not empty string\n")
    str = input("Put string for parsing: ")
print(ft_substr_qty(str))
