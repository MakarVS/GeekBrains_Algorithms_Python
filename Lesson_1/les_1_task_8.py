# Задача № 8.
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

try:
    numb_1 = float(input('Введите первое число: '))
    numb_2 = float(input('Введите второе число: '))
    numb_3 = float(input('Введите третье число: '))
except ValueError:
    print('Это не число!')
else:
    if numb_1 <= numb_2 <= numb_3:
        print(f'{numb_2} - среднее из чисел {numb_1}, {numb_2} и {numb_3}')
    elif numb_2 <= numb_1 <= numb_3:
        print(f'{numb_1} - среднее из чисел {numb_1}, {numb_2} и {numb_3}')
    else:
        print(f'{numb_3} - среднее из чисел {numb_1}, {numb_2} и {numb_3}')
