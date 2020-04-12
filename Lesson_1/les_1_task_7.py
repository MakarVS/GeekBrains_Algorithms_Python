# Задача № 7.
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = input('Введите год: ')

if year.isnumeric() and int(year) > 0:
    year = int(year)
    if (year % 4 != 0) or ((year % 100 == 0) and (year % 400 != 0)):
        print(f'Год {year} не является високосным')
    else:
        print(f'Год {year} является високосным')
else:
    print('Это не год после р.х.!')
