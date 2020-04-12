n = int(input('Введите кол-во предприятий: '))

comp_dict = {}
all_sum = 0

for _ in range(n):
    inp = input('Введите имя предприятия и прибыль за 4 квартала через пробел:\n').split(' ')
    comp_dict[inp[0]] = int(inp[1]) + int(inp[2]) + int(inp[3]) + int(inp[4])
    all_sum += int(inp[1]) + int(inp[2]) + int(inp[3]) + int(inp[4])

avg = all_sum / n

for name, profit in comp_dict.items():
    if profit >= avg:
        comp_dict[f'above_{name}'] = comp_dict.pop(name)
    else:
        comp_dict[f'below_{name}'] = comp_dict.pop(name)

print(f'Средняя прибыль за год всех предприятий - {avg}')
print('Предприятия с прибылью выше или равное среднему:')

for name, profit in comp_dict.items():
    if name.startswith('above'):
        print(f'{name[6:]} - годовая прибыль {profit}')

print('Предприятия с прибылью ниже среднего:')

for name, profit in comp_dict.items():
    if name.startswith('below'):
        print(f'{name[6:]} - годовая прибыль {profit}')

