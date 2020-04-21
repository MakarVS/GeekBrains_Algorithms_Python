'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
'''
import random

def ft_print_arr(arr):
    print(*arr, sep=", ")

def ft_arr_fill():
    n = int(input("Put array length: "))
    arr = [random.randint(0, 49) for x in range(n)]
    return (arr)

def ft_merge(arr, left, mid, right):
    qty1 = mid - left + 1
    qty2 = right - mid
    l_arr = [0] * (qty1)
    r_arr = [0] * (qty2)
    for i in range(0, qty1):
        l_arr[i] = arr[left + i]
    for j in range(0, qty2):
        r_arr[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while ((i < qty1) and (j < qty2)):
        if (l_arr[i] <= r_arr[j]):
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
        k += 1
    while (i < qty1):
        arr[k] = l_arr[i]
        i += 1
        k += 1
    while (j < qty2):
        arr[k] = r_arr[j]
        j += 1
        k += 1

def ft_merge_sort(arr, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        ft_merge_sort(arr, left, mid)
        ft_merge_sort(arr, mid + 1, right)
        ft_merge(arr, left, mid, right)

arr = ft_arr_fill()
print("Generated array: ")
ft_print_arr(arr)
ft_merge_sort(arr, 0, len(arr) - 1)
print("Sorted array: ")
ft_print_arr(arr)
