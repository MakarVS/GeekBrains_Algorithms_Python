from collections import OrderedDict


k = int(input('Кол-во предприятий  '))
enterprises = OrderedDict()

for i in range(1, k + 1):
    name = input('Название предприятия:    ')
    enterprises[name] = [float(input('Прибыль за первый квартал:  ')), float(input('Прибыль за второй квартал:  ')),
                         float(input('Прибыль за третий квартал:  ')), float(input('Прибыль за четвертый квартал:  '))]

    enterprises[name].append((enterprises[name][0] + enterprises[name][1]
                           + enterprises[name][2] + enterprises[name][3])/4)
print(enterprises)


average_revenue = 0
for key, value in enterprises.items():
    average_revenue += value[4]
average_revenue = round(average_revenue / k)


for key, value in enterprises.items():

    if value[4] > average_revenue:
        print(f' Предприятие {key}  заработало {value[1]}, что больше средней прибыли по отрасли {average_revenue}')
    elif value[4] < average_revenue:
        print(f' Предприятие {key}  заработало {value[1]}, что меньше средней прибыли по отрасли {average_revenue}')
    else:
        print(f' Предприятие {key}  заработало {value[1]}, что является средней приболью по отрасли ')







