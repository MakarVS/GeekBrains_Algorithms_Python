# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:24:03 2020

@author: Nekad
"""

# =============================================================================
# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
#  т. к. именно в этих позициях первого массива стоят четные числа.
# =============================================================================

import random
 

list_len = 10
 
#Создаем исходный массив при помощи генератора списков
num_lst = [random.randint(0, 11) for _ in range(list_len)]

#Называаем массив идексов четных чисел
even_num = []

# Для i-того элеманта в последовательности чисел от 0 до list_len
for i in range(list_len):
# Если элементс исходного массива с индексом i делиться без остатка на 0, то
     if num_lst[i] % 2 == 0:
# Записызываем индекст данного элемента в массив идексов четных чисел
         even_num.append(i + 1)
         
 
print(f'Исходный массив\n{num_lst}')
print(f'Массив идексов четных чисел\n{even_num}')

