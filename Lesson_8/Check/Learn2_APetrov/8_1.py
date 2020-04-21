#!/usr/bin/env python
# -*- coding: utf-8 -*-
# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

x=int(input('Введите количество человек: '))
spisok=[]
itogo=0
p=0
o=0
while p!=x:
	spisok.append([o for o in reversed(range(2+p,x+1))])
	itogo+=len(spisok[o])
	p+=1
	if x not in spisok[o]:
		print('Граф {} друга - пустой'.format(p))
	else:
		print('{} - граф {} друга.'.format(spisok[o],p))
	o+=1
print('Всего рукопожатий: ',itogo)
