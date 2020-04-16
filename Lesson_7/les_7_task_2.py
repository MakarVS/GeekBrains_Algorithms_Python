"""
Задача № 2.
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform


n = 10
array = [uniform(0, 49) for _ in range(n)]
print(f'Изначальный массив - {array}')


def sort_merge(array):
    """
    Сортировка методом слияния
    :param array: массив
    :return: отсортированный массив
    """
    if len(array) <= 1:
        return array[:]
    else:
        mid = len(array) // 2
        left_array = sort_merge(array[:mid])
        right_array = sort_merge(array[mid:])

        return merge(left_array, right_array)


def merge(left, right):
    """
    Промежуточная функция слияния двух отсортированных массивов
    :param left: левый массив
    :param right: правый массив
    :return: отсортированный слитый массив
    """
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


print(f'Отсортированный массив - {sort_merge(array)}')
