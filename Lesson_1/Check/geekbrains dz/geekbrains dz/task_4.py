alphabet = 'abcdefghijklmnopqrstuvwxyz'
x1 = input('1 буква ')
x2 = input('2 буква ')
n1 = alphabet.index(x1) + 1
n2 = alphabet.index(x2) + 1
dur = abs(n2-n1)-1
print(f'место буквы {x1} - {n1}')
print(f'место буквы {x2} - {n2}')
print(f'между ними букв - {dur}')