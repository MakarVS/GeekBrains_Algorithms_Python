"""
Задача № 3.
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

from random import randint, choice
import numpy as np

m = int(input('Введите натуральное число: '))
array = [randint(1, 100) for _ in range(2*m+1)]
print(f'Изначальный массив - {array}')


def find_median(array, k=len(array)/2):
    """
    Фукнция, использующая алгоритм быстрого выбора (quickselect) Хоара
    для нахождения k-ого наименьшего элемента массива
    :param array: массив
    :param k: по-умолчанию k-ым наименьшим элементом является индекс медианы
    :return: медиана массива
    """
    if len(array) == 1:
        return array[0]
    else:
        pivot = choice(array)

        below_pivot_array = [ar for ar in array if ar < pivot]
        above_pivot_array = [ar for ar in array if ar > pivot]
        pivot_array = [ar for ar in array if ar == pivot]

        if k < len(below_pivot_array):
            return find_median(below_pivot_array, k)
        elif k < len(below_pivot_array) + len(pivot_array):
            return pivot_array[0]
        else:
            return find_median(above_pivot_array, k - len(below_pivot_array) - len(pivot_array))


median = find_median(array)
# Проверка нахождения медианы со встроенной функцией
assert int(np.median(array)) == median, 'Медиана найдена не правильно!'
print(f'Медиана массива - {median}')
