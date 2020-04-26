"""
Задача № 1.
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечания:
- в сумму не включаем пустую строку и строку целиком;
- задача считается решённой, если в коде использована функция вычисления хеша
(hash(), sha1() или любая другая из модуля hashlib)
"""
import hashlib


def func(s):
    len_ = len(s)
    hash_set = set()
    for i in range(len_):
        for j in range(i, len_):
            hash_set.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

    return len(hash_set)


s = input('Введите строку: ')

print(f'Кол-во подстрок в строке "{s}" равно {func(s)}')
