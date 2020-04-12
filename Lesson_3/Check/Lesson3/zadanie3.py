# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# massiv=[1,2,0,5,3,21,3]
import random

massiv = random.sample(range(1, 100), 10)
print(massiv)

x=0
k=99999999
for i in massiv:
	if i>x:
		x=i
	if i<k:
		k=i
print(k,x)
min=massiv.index(k)
max=massiv.index(x)
print(max,min)
massiv.pop(min)
massiv.insert(min,x)
massiv.pop(max)
massiv.insert(max,k)
print(massiv)
