# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, надо вывести 6843.
x = int(input('Введите число: '))
i = 0
while x>0:
    i = i*10+x%10
    x = x//10
print(i)