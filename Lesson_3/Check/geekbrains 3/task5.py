"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""
from math import inf  # бесконечность
maxiotric = -inf
nums = list(map(int, input('заполните массив элементами через пробел \n').split()))
for i in nums:
    if 0 > i > maxiotric:
        maxiotric = i
print(f'искомый элемент {maxiotric}, его позиция - {nums.index(maxiotric)}')  # исчисление с 0
