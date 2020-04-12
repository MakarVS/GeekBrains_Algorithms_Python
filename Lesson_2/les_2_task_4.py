# Задача № 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите кол-во элементов ряда: '))

sum_el = 1
cur_el = 1

for i in range(1, n):
    cur_el /= -2
    sum_el += cur_el

print(f'Сумма ряда из {n} элементов равна {sum_el}')
