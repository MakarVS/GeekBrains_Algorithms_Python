'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой —
не больше медианы.
'''

import random
import numpy as np

def ft_print_arr(arr):
    print(*arr, sep=", ")

def ft_arr_fill():
    n = int(input("Put m for array length calculation (len = 2m + 1): "))
    arr = [random.randint(-100, 100) for x in range(2 * n + 1)]
    return (arr)

def ft_quickselect_median(arr, n, pivot_fn):
    if len(arr) == 1:
        return arr[0]
    pivot = pivot_fn(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if n < len(lows):
        return ft_quickselect_median(lows, n, pivot_fn)
    elif n < len(lows) + len(pivots):
        return pivots[0]
    else:
        return ft_quickselect_median(highs, n - len(lows) - len(pivots), pivot_fn)

arr = ft_arr_fill()
print("Generated array: ")
ft_print_arr(arr)
print("Median for generated array: {}".format(ft_quickselect_median(arr, len(arr) / 2, pivot_fn=random.choice)))
print(np.median(arr))
