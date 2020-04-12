# Задача № 3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def reverse(number, length, s):
    """Работает для реверса любой строки"""
    if length == 0:
        return s
    else:
        count = 1
        for num in number:
            if count == length:
                s += num
                length -= 1
                return reverse(number, length, s)
            else:
                count += 1


number = input('Введите натуральное число: ')

rev = reverse(number, len(number), '')
print(rev)
