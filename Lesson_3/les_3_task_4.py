# Задача № 4.
# Определить, какое число в массиве встречается чаще всего.

import random

lst = [random.randint(-2, 2) for i in range(1, 10)]
print(lst)


def count(lst):
    count_dct = {}
    for el in lst:
        try:
            count_dct[el] += 1
        except KeyError:
            count_dct[el] = 1
    return count_dct


count_dct = count(lst)
m = 0
max_el = 0
for el, count in count_dct.items():
    if count > m:
        m = count
        max_el = el

print(max_el)
