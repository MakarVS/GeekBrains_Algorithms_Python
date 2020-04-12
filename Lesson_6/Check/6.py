# -*- coding: utf-8 -*-
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import timeit
import sys
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Три реализации одного и того-же кода.
def code1():
	result = [0] * 8
	for i in range(2, 100):
		for j in range(2, 10):
			if i % j == 0:
				result[j - 2] += 1
	i = 0
	size=0
	size+=sys.getsizeof(result)
	size+=sys.getsizeof(i)
	size+=sys.getsizeof(j)
	return size
def code2():
	z=[99//i for i in range(2, 10)]
	size=sys.getsizeof(z)
	return size
n=0
def code3():
	for i in range(2,99):
		if n == 0:
			for l in range(2,9):
				if not i%l:
					x='число {} кратно {}'.format(i,l)
	size=0
	size+=sys.getsizeof(i)
	size+=sys.getsizeof(n)
	size+=sys.getsizeof(l)
	size+=sys.getsizeof(x)
	return size
time1=float('{:.6f}'.format(timeit.timeit(code1,number=1)))
size1=code1()
print('Первый код выполняется за {} секунд и его переменный занимают {} ячеек памяти'.format(time1,size1))
time2=float('{:.6f}'.format(timeit.timeit(code2,number=1)))
size2=code2()
print('Второй код выполняется за {} секунд и его переменный занимают {} ячеек памяти'.format(time2,size2))
time3=float('{:.6f}'.format(timeit.timeit(code3,number=1)))
size3=code3()
print('Третий код выполняется за {} секунд и его переменный занимают {} ячеек памяти'.format(time3,size3))
# Можем сделать вывод что второй код выполняется быстрее и занимает меньшее количество ячеек памяти,
# это связано с тем что он реализован как генератор в списке, и не нуждается в сторонних переменных
# Первый и третий код практически одинаковы, третий код занимает чуть больше памяти чем первый,
# это связано с тем что там используется больше переменных, этот код можно назвать избыточным.
