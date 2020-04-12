# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:01:37 2020

@author: Nekad
"""

# =============================================================================
# 4. Определить, какое число в массиве встречается чаще всего.
#Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.
# =============================================================================

import random


list_len = 10
min_item = 0
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(list_len)]
print(f'\nИсходный массив:\n{array}\n')

numbers = dict()

for item in array:

    if item not in numbers:
        numbers[item] = 1

    else:
        numbers[item] += 1

for i, j in numbers.items():
    print(f'Число {i} повторяется {j} раз(а)')

max_count = 0
num_max_count = []

for num in numbers:

    if numbers[num] > max_count:
        max_count = numbers[num]
        num_max_count = num

print(f'\nОдно из самых чаще всего повторящихся чисел: {num_max_count}')

