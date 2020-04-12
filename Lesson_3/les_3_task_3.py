# Задача № 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

lst = random.sample(range(1, 100), 10)
print(lst)


def min_max(lst):
    min_index = 0
    max_index = 0
    for i in range(len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
        if lst[i] > lst[max_index]:
            max_index = i
    return min_index, max_index


min_index, max_index = min_max(lst)
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
print(lst)
