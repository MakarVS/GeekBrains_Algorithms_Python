# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.


# Я выбрал для проверки задание 7 из ДЗ 2
# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

import timeit


def summ0(n):
    sum = 0
    for i in range(n):
        sum += i


def summ1(n):
    sum = 0
    for i in range(n):
        sum = sum + i


def summ2(n):
    sum = n * (n + 1) / 2

print(timeit.timeit("summ0(10)", setup="from __main__ import summ0", number=100000))
print(timeit.timeit("summ1(10)", setup="from __main__ import summ1", number=100000))
print(timeit.timeit("summ2(10)", setup="from __main__ import summ2", number=100000))
print()

print(timeit.timeit("summ0(100)", setup="from __main__ import summ0", number=100000))
print(timeit.timeit("summ1(100)", setup="from __main__ import summ1", number=100000))
print(timeit.timeit("summ2(100)", setup="from __main__ import summ2", number=100000))
print()

print(timeit.timeit("summ0(1000)", setup="from __main__ import summ0", number=100000))
print(timeit.timeit("summ1(1000)", setup="from __main__ import summ1", number=100000))
print(timeit.timeit("summ2(1000)", setup="from __main__ import summ2", number=100000))
print()

print(timeit.timeit("summ0(10000)", setup="from __main__ import summ0", number=100000))
print(timeit.timeit("summ1(10000)", setup="from __main__ import summ1", number=100000))
print(timeit.timeit("summ2(10000)", setup="from __main__ import summ2", number=100000))

# Выводы:
# 1) Выражения (a += i) и (a = a + i) не отличаются в скорости
# 2) Первые два алгоритма подсчета суммы арифмитической последовательности имеют линейную сложность O(n)
#    Это и ожидалось, ведь алгоритму надо пройти по всем элементам последовательности
# 3) Третий алгоритм всегда выполняется за константное время O(1), т.к. независимо от числа элементов используется
#    общая формула подсчета суммы последовательности
# Итого: зачастую можно найти гораздо более изящный и быстрый способ решить задачу. Прежде чем писать код - надо подумать.
# Был выбран очень простой пример, который даже сложно назвать алгоритмом, но суть он передает.