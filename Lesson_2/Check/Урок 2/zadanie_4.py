# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите число преобразований: '))
cifra=itog=i=1
while i<n:
   cifra/=-2
   itog+=cifra
   i+=1
print(itog)