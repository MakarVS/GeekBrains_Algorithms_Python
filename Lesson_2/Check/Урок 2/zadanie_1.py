# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции. 
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
while True:
    a=float(input('Введите первое число: '))
    b=float(input('Введите второе число: '))
    print('0 - выход из программы')
    znak=input('Введите знак операции(0, +, -, *, /): ')
    if znak == '/':
        if b == 0:
            print('Невозможно делить на ноль')
            continue
        vivod=a/b
    elif znak == '*':
        vivod=a*b
    elif znak == '-':
        vivod=a-b
    elif znak == '+':
        vivod=a+b
    elif znak == '0':
        break
    else:
        print('Введенно неверное значение, попробуйте ещё раз')
        continue
    print(vivod)
print('Выход из программы')