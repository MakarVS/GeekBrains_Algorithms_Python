"""
 В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
"""
from math import inf  # бесконечность
maxi = -inf
mini = inf
nums = list(map(int, input('заполните массив элементами через пробел \n').split()))
for i in nums:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print(f'максимальный элемент nums[{nums.index(maxi)}] = {maxi}\nминимальный элемент nums[{nums.index(mini)}] = {mini} \n')
if nums.index(maxi) > nums.index(mini):
    start = nums.index(mini)
    finish = nums.index(maxi)
else:
    finish = nums.index(mini)
    start = nums.index(maxi)
nums2 = nums[(start + 1):finish]
sum = 0
for i in nums2:
    sum += i
print('сумма', sum)