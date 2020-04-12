#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.
# massiv=[1,2,0,5,3,21,3]
import random

massiv = [random.randint(-10, 10) for i in range(1, 10)]

print(massiv)
x=0
k=99999999
itogo=0
for i in massiv:
	if i>x:
		x=i
	if i<k:
		k=i
for j in massiv:
	if j<x and j>k:
		itogo+=j
print('сумма элементов: {}'.format(itogo))
		