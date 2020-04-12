# Задача № 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple, deque


n = int(input('Введите кол-во предприятий: '))

company = namedtuple('Company', 'profit_1 profit_2 profit_3 profit_4')
comp_dict = {}
all_sum = 0

for _ in range(n):
    inp = input('Введите имя предприятия и прибыль за 4 квартала через пробел:\n').split(' ')
    name = inp[0]
    profit_list = [float(profit) for profit in inp[1:]]
    comp_dict[name] = company(*profit_list)
    all_sum += sum(profit_list)

avg = all_sum / n

fin_deq = deque()
max_below = 0
name_lim = ''

for name, profit in comp_dict.items():
    year_profit = sum(profit)
    if year_profit >= avg:
        fin_deq.append(name)
    else:
        if year_profit > max_below:
            max_below = profit
            name_lim = name
        fin_deq.appendleft(name)

print(f'Средняя прибыль за год всех предприятий - {avg}')
print('Предприятия с прибылью выше или равное среднему:')

for i in range(len(fin_deq)-1, -1, -1):
    name = fin_deq[i]
    if name == name_lim:
        print('Предприятия с прибылью ниже среднего:')
    print(f'{name} - годовая прибыль {sum(comp_dict[name])}')

# Данную программу можно написать без использования коллекций впрнципе, как минимум без очереди,
# просто итерируясь по отсортированному по сумме прибыли словарю и сравнивая сразу годовую прибыль со средним.
# Программа ниразу не оптимизированная - я в курсе. Просто пытался по максимому использовать коллекции из модуля.
