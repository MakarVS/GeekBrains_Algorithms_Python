# Задача № 6.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

lst = [random.randint(-10, 10) for i in range(1, 10)]
print(f'Исходные массив {lst}')

ind_mn = 0
ind_mx = len(lst) - 1
for i in range(len(lst)):
    if lst[i] < lst[ind_mn]:
        ind_mn = i
    elif lst[i] > lst[ind_mx]:
        ind_mx = i

print(f'Минимальный элемент {lst[ind_mn]} под индексом {ind_mn}')
print(f'Максимальный элемент {lst[ind_mx]} под индексом {ind_mx}')

if ind_mn > ind_mx:
   ind_mn, ind_mx = ind_mx, ind_mn

sum_ = 0
for i in range(ind_mn+1, ind_mx):
    sum_ += lst[i]

print(f'Сумма элементов между минимальным и максимальным элементами массива равна {sum_}')
