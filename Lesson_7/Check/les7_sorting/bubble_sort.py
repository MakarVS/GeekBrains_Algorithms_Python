'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка
пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''

import random
import time

def ft_print_arr(arr):
    print(*arr, sep=", ")

def ft_arr_fill():
    n = int(input("Put array length: "))
    arr = [random.randint(-100, 99) for x in range(n)]
    return (arr)

def ft_bubble_sort(arr):
    print("\na) Full iteration data:")
    start = time.time()
    compare, swap = 0, 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if (arr[j + 1] > arr[j]):
                arr[j + 1], arr[j] =  arr[j], arr[j + 1]
                swap += 1
            compare += 1
    end = time.time()
    ft_print_arr(arr)
    print("Operation time: %s seconds" % (round(end - start, 10)))
    print("Comparisons: {}, swaps: {}".format(compare, swap))

def ft_opt_bubble_sort(arr):
    print("\nb) Optimized iteration data:")
    start = time.time()
    compare, swap = 0, 0
    n = len(arr) - 1
    while (n):
        need_swap = False
        for i in range(0, n):
            if arr[i + 1] > arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                need_swap = True
                swap += 1
            compare += 1
        if not (need_swap):
            break
        n -= 1
    end = time.time()
    ft_print_arr(arr)
    print("Operation time: %s seconds" % (round(end - start, 10)))
    print("Comparisons: {}, swaps: {}".format(compare, swap))

arr = ft_arr_fill()
arr_cpy = arr.copy()
print("Generated array: ")
ft_print_arr(arr)
print("\nSorted array: ")
ft_bubble_sort(arr)
ft_opt_bubble_sort(arr_cpy)

