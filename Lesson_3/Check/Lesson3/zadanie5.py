#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
massiv=[1,3,87,-2,-9,-87,6,-89]
# massiv = [10, -1, 0, 6, 10, -6, 8, 3, 9]
# import random

# massiv = [random.randint(-10, 10) for i in range(1, 10)]
print(massiv)

otric=[]
x=0
for list in massiv:
	list=str(list)
	if '-' in list:
		list=list[1:]
		otric.append(list)
for last in otric:
	last=int(last)
	if last>x:
		x=last
x='-'+str(x)
x=int(x)
index=massiv.index(x)
print('максимальный отрицательный элемент {}, его позиция в массиве: {}'.format(x,index))