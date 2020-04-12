# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:40:12 2020

@author: Nekad
"""

# =============================================================================
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# =============================================================================

import random


list_len = 10
min_item = 0
max_item = 150

#Создаем массив случайных целых чисел
array = [random.randint(min_item, max_item) for _ in range(list_len)]
print(f'\nИсходный массив:\n{array}')

num_min = array[0]
min_index = 0
num_max = array[0]
max_index = 0

for i, item in enumerate(array):
    if item < num_min:
        num_min = item
        min_index = i
    elif item > num_max:
        num_max = item
        max_index = i

print(f'\nМеняем максимальное число {num_max} с индексом {max_index} местами с минимальным числом {num_min} с индексом {min_index}.\n')

array[max_index], array[min_index] = array[min_index], array[max_index]
print(f'Новый массив:\n{array}')

