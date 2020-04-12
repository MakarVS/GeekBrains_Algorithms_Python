# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict, deque
from copy import copy

sixt_def = defaultdict(int)
rev_sixt_def = defaultdict(int)

sixt = {'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15}

rev_sixt = {10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'}

sixt_def.update(sixt)
rev_sixt_def.update(rev_sixt)


def get_val(def_dict, val):
    """
    Функция возвращает соответствие шестнадцатеричному числу - десятичное и наоборот.
    Фактически можно было составить полные словари со всеми цифрами, но мне было лень это делать. Код писать интереснее.
    :param def_dict: словарь
    :param val: ключ
    """
    if def_dict[val]:
        return def_dict[val]
    else:
        return val


def hex_sum(num_1, num_2):
    """
    Функция для суммирования двух шестнадцатеричных чисел
    :param num_1: первое число
    :param num_2: второе число
    """

    def hex_buf_operation_sum(a, b, remember_sum):
        """
        Дополнительная функция для суммирования двух цифр и запоминания разряда
        :param a: первая цифра
        :param b: вторая цифра
        :param remember_sum: перенос в следующий разряд (один в уме =) )
        :return: следующий запомненный разряд (либо 0 по-умолчанию, либо 1 при переносе)
        """
        a = int(get_val(sixt_def, a))
        b = int(get_val(sixt_def, b))

        summ = a + b + remember_sum

        if summ < 16:
            answer_sum.appendleft(get_val(rev_sixt_def, summ))
            remember_sum = 0
        else:
            remember_sum = 1
            answer_sum.appendleft(get_val(rev_sixt_def, summ - 16))

        return remember_sum

    sum_num_1 = copy(num_1)
    sum_num_2 = copy(num_2)
    answer_sum = deque()

    remember_sum = 0

    while sum_num_2:
        # Будем из очередей-чисел брать справа по одной цифре, удаляя ее из числа, пока во 2 числе не останется цифр.
        remember_sum = hex_buf_operation_sum(sum_num_1.pop(), sum_num_2.pop(), remember_sum)

    # Возможна ситуация, когда 2-ое число меньше первого на несколько цифр и у 1-ого еще остались цифры.
    # Оставшиеся цифры нужно сложить с запомненным разрядом.
    while sum_num_1:
        remember_sum = hex_buf_operation_sum(sum_num_1.pop(), remember_sum, 0)

    if remember_sum:
        # И в конце при существовании запомненного разряда - добавляем его к числу
        answer_sum.appendleft(get_val(rev_sixt_def, remember_sum))

    return [str(i) for i in answer_sum]


def hex_mult(num_1, num_2):
    """
    Функция для умножения двух шестнадцатеричных чисел
    :param num_1: первое число
    :param num_2: второе число
    :return:
    """
    def hex_buf_oper_1(a, b, remember_mult, deq):
        """
        Дополнительная функция для умножения цифры на цифру с запоминанием разряда
        :param a: первая цифра
        :param b: вторая цифра
        :param remember_mult: разряд
        :param deq: очередь к которой прибавлять ответ
        :return:
        """
        a = int(get_val(sixt_def, a))
        b = int(get_val(sixt_def, b))

        mult = a * b + remember_mult

        if mult < 16:
            deq.appendleft(get_val(rev_sixt_def, mult))
            remember_mult = 0
        else:
            remember_mult = mult // 16
            deq.appendleft(get_val(rev_sixt_def, mult % 16))

        return remember_mult

    def hex_buf_oper_2(deq, mult_num_1, buf_num_2, remember_mult, count):
        """
        Дополнительная функция для перемножения одного числа на одну цифру из другого числа
        :param deq: очередь
        :param mult_num_1: число
        :param buf_num_2: цифра
        :param remember_mult: разряд в уме
        :param count: счетчик умножения числа на цифру (нужен для добавления в конец промежуточных чисел нулей)
        :return:
        """
        for i in range(1, len(mult_num_1) + 1):
            remember_mult = hex_buf_oper_1(mult_num_1[-i], buf_num_2, remember_mult, deq)
        deq.appendleft(get_val(rev_sixt_def, remember_mult))
        if count:
            deq.extend(['0'] * count)

    mult_num_1 = copy(num_1)
    mult_num_2 = copy(num_2)

    count = 0
    count_oper_2 = 0
    buf_deque_1, buf_deque_2 = deque([]), deque([])

    while mult_num_2:
        if count == 0:
            buf_deque_1 = deque([])
            buf_num_2 = mult_num_2.pop()
            remember_mult = 0
            hex_buf_oper_2(buf_deque_1, mult_num_1, buf_num_2, remember_mult, count_oper_2)
            count += 1
            count_oper_2 += 1
        elif count % 2 == 0:
            buf_deque_1, buf_deque_2 = sorted([buf_deque_1, buf_deque_2], key=len, reverse=True)
            buf_deque_1 = hex_sum(buf_deque_1, buf_deque_2)
            count += 1
        else:
            remember_mult = 0
            buf_deque_2 = deque([])
            buf_num_2 = mult_num_2.pop()
            hex_buf_oper_2(buf_deque_2, mult_num_1, buf_num_2, remember_mult, count_oper_2)
            count += 1
            count_oper_2 += 1

    buf_deque_1, buf_deque_2 = sorted([buf_deque_1, buf_deque_2], key=len, reverse=True)
    buf_deque_1 = hex_sum(buf_deque_1, buf_deque_2)

    return [str(i) for i in buf_deque_1]


str_num_1 = input('Введите первое число: ').lower()
str_num_2 = input('Введите второе число: ').lower()
num_1 = list(str_num_1)
num_2 = list(str_num_2)

# num_1 = deque(['b', '3', 'a', '5', 'e'])
# num_2 = deque(['3', 'd', 'f'])

# num_1 = deque(['a', '8', '6', 'b', '8', '2'])
# num_2 = deque(['9', '1', 'f', '6', 'c', '6', '0'])

# Сортируем числа. Первое число будет всегда больше или равно второго.
num_1, num_2 = sorted([num_1, num_2], key=len, reverse=True)

answer_sum = hex_sum(num_1, num_2)
answer_mult = hex_mult(num_1, num_2)

# ВНИМАНИЕ! Изначально ответы в виде списка, только здесь преобразую с помощью join в строку для удобства чтения.
print(f"{str_num_1.upper()} + {str_num_2.upper()} = {''.join(answer_sum).upper()}")
print(f"{str_num_1.upper()} * {str_num_2.upper()} = {''.join(answer_mult).upper()}")
