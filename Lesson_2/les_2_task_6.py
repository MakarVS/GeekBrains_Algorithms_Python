# Задача № 6.
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.


import random

number = random.randint(0, 100)


def guess(number):
    for i in range(10, 0, -1):
        print(f'Осталось {i} попыток!')
        user_number = int(input('Введите число: '))
        if number == user_number:
            return print(f'Верно! Вы угадали число {number}!')
        else:
            if user_number > number:
                sign = 'больше'
            else:
                sign = 'меньше'
            print(f'{user_number} {sign} загаданного!')
    return print(f'Ваши попытки закончились! Вы не угадали! Загаданное число - {number}')


guess(number)
