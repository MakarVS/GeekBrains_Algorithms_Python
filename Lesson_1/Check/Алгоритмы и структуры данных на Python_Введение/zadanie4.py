# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
bukvi=('abcdefghijklmnopqrstuvwxyz')
a=input('Введите первую букву: ')
b=input('Введите вторую букву: ')
granica_1=bukvi.find(a)
granica_2=bukvi.find(b)
dlina=granica_2-granica_1-1
print('Буква {} имеет номер {} в алфавите'.format(a,granica_1+1))
print('Буква {} имеет номер {} в алфавите'.format(b,granica_2+1))
print(dlina)