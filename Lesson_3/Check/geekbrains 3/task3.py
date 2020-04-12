"""
В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
"""
from random import randint

mass = [randint(1, 100) for i in range(int(input('введите длину массива случайных чисел ')))]
print('исходный массив', mass)
mini = 101
maxi = 0
indexmini = None
indexmaxi = None
for i in range(len(mass)):
    if mass[i] > maxi:
        indexmaxi = i
        maxi = mass[i]
    if mass[i] < mini:
        indexmini = i
        mini = mass[i]
mass[indexmini], mass[indexmaxi] = maxi, mini
print(f'поменяли местами {mini} и {maxi}')
print('измененный', mass)
