# Задача № 5.
#  В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

lst = [random.randint(-10, 10) for i in range(1, 10)]

flag_non_first = True
m = 0
for i in range(len(lst)):
    if lst[i] < 0 and flag_non_first:
        m = lst[i]
        ind = i
        flag_non_first = False
    elif m < lst[i] < 0:
        m = lst[i]
        ind = i

print(lst)
print(f'Элемент {m} под индексом {ind}')
