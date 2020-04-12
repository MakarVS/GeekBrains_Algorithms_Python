"""
определить какое число в массиве встечается чаще всего
"""


mass = list(map(int, input('заполните массив элементами через пробел \n').split()))
list_of_values = tuple(set(mass))
counttings = [0] * len(list_of_values)
for i in range(len(list_of_values)):
    counttings[i] = mass.count(list_of_values[i])
maxi = 0
answer = None
for i in range(len(counttings)):
    if counttings[i] > maxi:
        maxi = counttings[i]
        answer = list_of_values[i]
print('чаще всего встречается', answer)