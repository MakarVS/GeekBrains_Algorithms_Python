# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:56:46 2020

@author: Nekad
"""

# =============================================================================
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# =============================================================================

import random

list_len = 10
min_item = -100
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(list_len)]
print(f'\nИсходный массив:\n{array}\n')

max_negative_num = 0

for i, item in enumerate(array):

    if item < 0 and max_negative_num == 0:
        max_negative_num = item
        num_index = i

    elif max_negative_num < item < 0:
        max_negative_num = item
        num_index = i

if max_negative_num == 0:
    print('Отрицательных элементов не найдено.')

else:
    print(f'Максимальный отрицательный элемент: {max_negative_num}\nПозиция по порядку в массиве максимального отрицательного элемента: {num_index+1}\nИндекс в массиве максимального отрицательного элемента: {num_index}')
    
    