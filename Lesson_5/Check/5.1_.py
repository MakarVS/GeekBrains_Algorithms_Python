#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################
#			Задание № 1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
##############################################
# import collections
# print('-'*15,'Задание #1','-'*15,'\n')
# n=int(input('Введите количество предприятий: '))
# i=0
# nazvanie=[] # Блок с именами предприятия
# kvartal_1=[]
# kvartal_2=[]
# kvartal_3=[]
# kvartal_4=[]
# summa=[]
# minim=[]
# maxim=[]
# sr_pr=0
# # Цикл на ввод данных от пользователя
# while n>i:
# 	nazvanie.append(input('Введите название предприятия: '))
# 	kvartal_1.append(int(input('Введите прибыль за 1 квартал: ')))
# 	kvartal_2.append(int(input('Введите прибыль за 2 квартал: ')))
# 	kvartal_3.append(int(input('Введите прибыль за 3 квартал: ')))
# 	kvartal_4.append(int(input('Введите прибыль за 4 квартал: ')))
# 	i+=1
# # Цикл на подсчёт средней прибыли
# print('\n')
# i=0
# while n>i:
# 	summa.append((kvartal_1[i]+kvartal_2[i]+kvartal_3[i]+kvartal_4[i])/4)
# 	i+=1
# # Цикл на вычисления средней суммы
# i=0
# while n>i:
# 	sr_pr+=summa[i]
# 	i+=1
# sr_pr/=n
# print('Средняя сумма всех предприятий: ', sr_pr)
# # Цикл на создание словарей минимума и максимума
# i=0
# while n>i:
# 	if summa[i] > sr_pr:
# 		maxim.append(nazvanie[i])
# 	elif summa[i] < sr_pr:
# 		minim.append(nazvanie[i])
# 	else:
# 		jet='Предприятие {} за год заработало среднее значение: {}'.format(nazvanie[i],sr_pr)
# 	i+=1
# # Цикл на вывод данных о предприятии
# i=0
# while n>i:
# 	print('Средняя прибыль предприятия {}: {}'.format(nazvanie[i],summa[i]))
# 	i+=1
# if minim and maxim != False:
# 	print('Меньше среднего заработали: ')
# 	i=0
# 	while len(minim)>i:
# 		print(minim[i])
# 		i+=1
# 	i=0
# 	print('Больше среднего заработали: ')
# 	while len(maxim)>i:
# 		print(maxim[i])
# 		i+=1
##############################################
#			Задание № 2
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
##############################################
# print('\n','-'*15,'Задание #2','-'*15,'\n')
def convertto(massiv):
# Конвертируем заданные значения в десятичную систему
	chislo=[]
	for i in massiv:
		if i==0:
			chislo.append(0)
		elif i=='1':
			chislo.append(1)
		elif i=='2':
			chislo.append(2)
		elif i=='3':
			chislo.append(3)
		elif i=='4':
			chislo.append(4)
		elif i=='5':
			chislo.append(5)
		elif i=='6':
			chislo.append(6)
		elif i=='7':
			chislo.append(7)
		elif i=='8':
			chislo.append(8)
		elif i=='9':
			chislo.append(9)
		elif i=='A':
			chislo.append(10)
		elif i=='B':
			chislo.append(11)
		elif i=='C':
			chislo.append(12)
		elif i=='D':
			chislo.append(13)
		elif i=='E':
			chislo.append(14)
		elif i=='F':
			chislo.append(15)
		else:
			print('Нет такой цифры в шестнадцатеричном формате')
	x=len(massiv)-1
	j=0
	summa=0
	while x!=-1:
		summa+=(16**x)*chislo[j]
		j+=1
		x-=1
	return summa
def toconvert(massiv):
# Конвертируем наш результат в шестнадцатеричную СС
	ostatok=[]
	chislo=[]
	itogo=[]
	while massiv != 0:
		ostatok.append(massiv%16)
		massiv//=16
	for i in ostatok:
		if i==0:
			chislo.append('0')
		elif i==1:
			chislo.append('1')
		elif i==2:
			chislo.append('2')
		elif i==3:
			chislo.append('3')
		elif i==4:
			chislo.append('4')
		elif i==5:
			chislo.append('5')
		elif i==6:
			chislo.append('6')
		elif i==7:
			chislo.append('7')
		elif i==8:
			chislo.append('8')
		elif i==9:
			chislo.append('9')
		elif i==10:
			chislo.append('A')
		elif i==11:
			chislo.append('B')
		elif i==12:
			chislo.append('C')
		elif i==13:
			chislo.append('D')
		elif i==14:
			chislo.append('E')
		elif i==15:
			chislo.append('F')
	i=-1
	j=len(chislo)-1
	while j!=i:
		itogo.append(chislo[j])
		j-=1
	return itogo
a=list(input('Введите первое число(в шестнадцатеричном формате): '))
b=list(input('Введите второе число(в шестнадцатеричном формате): '))
c=input('Введите знак операции: ')
# Шестнадцатеричная в двоичную и десятичную
x=convertto(b)
y=convertto(a)
if c == '/':
	itog=x/y
elif c=='+':
	itog=x+y
elif c == '-':
	itog=x-y
elif c == '*':
	itog=x*y
else:
	print('Нет такой операции.\nВыход из программы')
print('Вывод в шестнадцатеричном формате: {}'.format(toconvert(itog)))
print('Число в двоичном формате: {}'.format(itog))
