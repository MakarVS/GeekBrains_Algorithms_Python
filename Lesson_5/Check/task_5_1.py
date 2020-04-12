# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from  collections import deque,OrderedDict


c ={}
j =[]
z = {}
l=deque([],maxlen=1)
a = int(input('введите кол-во предприятий: '))
d = deque([],maxlen=a)
def firm():

    d.append(firm)

    for i in range(a):
        name = input(str(i + 1) + '-е предприятие: ')
        c['name'] = name

        profit_1 = int(input('прибыль за первый квартал: '))
        j.append(profit_1)
        c['1й квартал'] = profit_1
        profit_2 = int(input('прибыль за второй квартал:  '))
        j.append(profit_2)
        c['2й квартал'] = profit_2
        profit_3 = int(input('прибыль за третий квартал:  '))
        j.append(profit_3)
        c['3й квартал'] = profit_3
        profit_4 = int(input('прибыль за четвертый квартал:  '))
        j.append(profit_4)
        c['4й квартал'] = profit_4
        c['средняя прибыль предприятия за год'] = [(profit_1 + profit_2 + profit_3 + profit_4) // 12]
        d.append(c)
        z[name] = (profit_1+profit_2+profit_3+profit_4)//12

        l.append(z)
    return

firm()

sr = sum(j)//(12+a)
print(f'средняя прибыль всех предприятий за год:  {sr}')

list_z = OrderedDict(z)

for i in list_z:
    if list_z[i] > sr:
        print(f'эта организация имеет доход больше среднего :  {i,list_z[i]}')
    else:
        print(f'эта организация имеет доход меньше среднего :  {i,list_z[i]}')























