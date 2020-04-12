# Задача № 1.
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в
# файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# Взята 1 задача из 5 урока:
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

# Данная задача взята из-за следующих соображений. По-моему мнению задача не соответствовала теме урока, коллекции
# были в ней притянуты за уши и решалась она спокойно без них. Хочется проверить свое утверждение с точки зрения,
# занимаемой памяти.
import sys
from collections import namedtuple, deque


# print(sys.version, sys.platform)
# 3.7.1 (default, Oct 23 2018, 14:07:42)
# [Clang 4.0.1 (tags/RELEASE_401/final)] darwin - MacOS
# Так как в данном коде не использован модуль struct, то разрядность не важна.


def show_all_size(vars_):
    """
    Функция для определения суммарного размера всех локальных переменных функции
    :param vars_: словарь локальных переменных и их значений
    :return:
    """
    def show_size_object(x, sum_=0):
        """
        Немного модифицированная рекурсивная функция из лекции для определения суммарного размера объекта
        :param x: объект
        :param sum_: суммарный размер в байтах
        :return: суммарный размер в байтах
        """
        sum_ += sys.getsizeof(x)
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for xx in x.items():
                    sum_ = show_size_object(xx, sum_)
            elif not isinstance(x, str):
                try:
                    for xx in x:
                        sum_ = show_size_object(xx, sum_)
                # Некоторые объекты типа объекта класса namedtuple хоть и имеют метод __iter__ не итерируемые.
                except TypeError:
                    pass
        return sum_
    print('Оценка затратов памяти:')
    all_sum = 0
    for name, val in vars_.items():
        # В перечне локальных переменных также есть функция для подсчета размера, убираем ее
        if name != 'size_of':
            current_mem = show_size_object(val)
            all_sum += current_mem
            print(f'Суммарный размер {name} класса {val.__class__} - {current_mem} байт')
    print('-'*50)
    print(f'Общая занимаемая память всеми переменными, оставшимеся в памяти - {all_sum} байт')

# Теперь в каждую функцию добавляем в качестве необязательного аргумента нашу функцию для подсчета размера и
# также пару строчек кода, которые вызывают эту функцию, если она передана


# Первая версия (изначальная)
def version_with_collections(size_of=None):
    n = int(input('Введите кол-во предприятий: '))

    company = namedtuple('Company', 'profit_1 profit_2 profit_3 profit_4')
    comp_dict = {}
    all_sum = 0

    for _ in range(n):
        inp = input('Введите имя предприятия и прибыль за 4 квартала через пробел:\n').split(' ')
        name = inp[0]
        profit_list = [float(profit) for profit in inp[1:]]
        comp_dict[name] = company(*profit_list)
        all_sum += sum(profit_list)

    avg = all_sum / n

    fin_deq = deque()
    max_below = 0
    name_lim = ''

    for name, profit in comp_dict.items():
        year_profit = sum(profit)
        if year_profit >= avg:
            fin_deq.append(name)
        else:
            if year_profit > max_below:
                max_below = sum(profit)
                name_lim = name
            fin_deq.appendleft(name)

    print(f'Средняя прибыль за год всех предприятий - {avg}')
    print('Предприятия с прибылью выше или равное среднему:')

    for i in range(len(fin_deq) - 1, -1, -1):
        name = fin_deq[i]
        if name == name_lim:
            print('Предприятия с прибылью ниже среднего:')
        print(f'{name} - годовая прибыль {sum(comp_dict[name])}')

    # Добавил в свое старое решение следующие строчки кода
    if size_of:
        # locals() представляет собой словарь всех локальных переменных
        size_of(locals())


# Вторая версия (примем допущение, что как в и прошлом варианте необходимо хранить все промежуточные прибыли
# за каждый квартал). Однако, в этой версии вместо namedtuple используем словарь, а вместо очереди список.
# Остальные переменные оставили по-максимому нетронутами.
def version_without_collections(size_of=None):
    n = int(input('Введите кол-во предприятий: '))

    comp_dict = {}
    all_sum = 0

    for _ in range(n):
        inp = input('Введите имя предприятия и прибыль за 4 квартала через пробел:\n').split(' ')
        name = inp[0]
        comp_dict[name] = {'profit_1': int(inp[1]), 'profit_2': int(inp[2]),
                           'profit_3': int(inp[3]), 'profit_4': int(inp[4])}
        all_sum += sum(comp_dict[name].values())

    avg = all_sum / n

    fin_list = []
    max_below = 0
    name_lim = ''

    for name, profit in comp_dict.items():
        year_profit = sum(profit.values())
        if year_profit >= avg:
            fin_list.append(name)
        else:
            if year_profit > max_below:
                max_below = sum(profit.values())
                name_lim = name
            fin_list.insert(0, name)

    print(f'Средняя прибыль за год всех предприятий - {avg}')
    print('Предприятия с прибылью выше или равное среднему:')

    for i in range(len(fin_list) - 1, -1, -1):
        name = fin_list[i]
        if name == name_lim:
            print('Предприятия с прибылью ниже среднего:')
        print(f'{name} - годовая прибыль {sum(comp_dict[name].values())}')

    # Измеряем память
    if size_of:
        # locals() представляет собой словарь всех локальных переменных
        size_of(locals())


# Третья версия. На самом деле нигде в условии задачи не сказано, что нужно хранить прибыль за каждый квартал.
# Поэтому будем хранить только годовую прибыль предприятия. Данная версия будет использовать лишь один словарь и
# перезапишет его, когда нужно будет разделить предприятия по порогу добавив в их имена приставки above и below для
# возмоджности дальнейшего разделения. В этой версии стараюсь использовать минимальное число переменных.
def version_with_one_dict(size_of=None):
    n = int(input('Введите кол-во предприятий: '))

    comp_dict = {}
    all_sum = 0

    for _ in range(n):
        inp = input('Введите имя предприятия и прибыль за 4 квартала через пробел:\n').split(' ')
        comp_dict[inp[0]] = int(inp[1]) + int(inp[2]) + int(inp[3]) + int(inp[4])
        all_sum += int(inp[1]) + int(inp[2]) + int(inp[3]) + int(inp[4])

    avg = all_sum / n

    for name, profit in comp_dict.items():
        if profit >= avg:
            comp_dict[f'above_{name}'] = comp_dict.pop(name)
        else:
            comp_dict[f'below_{name}'] = comp_dict.pop(name)

    print(f'Средняя прибыль за год всех предприятий - {avg}')
    print('Предприятия с прибылью выше или равное среднему:')

    for name, profit in comp_dict.items():
        if name.startswith('above'):
            print(f'{name[6:]} - годовая прибыль {profit}')

    print('Предприятия с прибылью ниже среднего:')

    for name, profit in comp_dict.items():
        if name.startswith('below'):
            print(f'{name[6:]} - годовая прибыль {profit}')

    # Измеряем память
    if size_of:
        # locals() представляет собой словарь всех локальных переменных
        size_of(locals())

# Затраты памяти проверялись на следующих входных данных:
# Кол-во предприятий = 3
# Первое предприятие: asd 1 2 3 4
# Второе предприятие: qwe 2 3 4 5
# Третье предприятие: zxc 3 3 4 5

# Вызов начальной версии
# version_with_collections(show_all_size)

# Оценка затратов памяти:
# Суммарный размер n класса <class 'int'> - 28 байт
# Суммарный размер company класса <class 'type'> - 888 байт
# Суммарный размер comp_dict класса <class 'dict'> - 1116 байт
# Суммарный размер all_sum класса <class 'float'> - 24 байт
# Суммарный размер _ класса <class 'int'> - 28 байт
# Суммарный размер inp класса <class 'list'> - 412 байт
# Суммарный размер name класса <class 'str'> - 52 байт
# Суммарный размер profit_list класса <class 'list'> - 192 байт
# Суммарный размер avg класса <class 'float'> - 24 байт
# Суммарный размер fin_deq класса <class 'collections.deque'> - 788 байт
# Суммарный размер max_below класса <class 'float'> - 24 байт
# Суммарный размер name_lim класса <class 'str'> - 52 байт
# Суммарный размер profit класса <class '__main__.Company'> - 176 байт
# Суммарный размер year_profit класса <class 'float'> - 24 байт
# Суммарный размер i класса <class 'int'> - 24 байт
# --------------------------------------------------
# Общая занимаемая память всеми переменными, оставшимеся в памяти - 3852 байт

# Вызов второй версии
# version_without_collections(show_all_size)

# Оценка затратов памяти:
# Суммарный размер n класса <class 'int'> - 28 байт
# Суммарный размер comp_dict класса <class 'dict'> - 3096 байт
# Суммарный размер all_sum класса <class 'int'> - 28 байт
# Суммарный размер _ класса <class 'int'> - 28 байт
# Суммарный размер inp класса <class 'list'> - 412 байт
# Суммарный размер name класса <class 'str'> - 52 байт
# Суммарный размер avg класса <class 'float'> - 24 байт
# Суммарный размер fin_list класса <class 'list'> - 252 байт
# Суммарный размер max_below класса <class 'int'> - 28 байт
# Суммарный размер name_lim класса <class 'str'> - 52 байт
# Суммарный размер profit класса <class 'dict'> - 836 байт
# Суммарный размер year_profit класса <class 'int'> - 28 байт
# Суммарный размер i класса <class 'int'> - 24 байт
# --------------------------------------------------
# Общая занимаемая память всеми переменными, оставшимеся в памяти - 4888 байт

# Вызов третьей версии
# version_with_one_dict(show_all_size)

# Оценка затратов памяти:
# Суммарный размер n класса <class 'int'> - 28 байт
# Суммарный размер comp_dict класса <class 'dict'> - 690 байт
# Суммарный размер all_sum класса <class 'int'> - 28 байт
# Суммарный размер _ класса <class 'int'> - 28 байт
# Суммарный размер inp класса <class 'list'> - 412 байт
# Суммарный размер avg класса <class 'float'> - 24 байт
# Суммарный размер name класса <class 'str'> - 58 байт
# Суммарный размер profit класса <class 'int'> - 28 байт
# --------------------------------------------------
# Общая занимаемая память всеми переменными, оставшимеся в памяти - 1296 байт

'''
При анализе трех алгоритмов можно сделать следующие выводы:
1. Сравнивая первую и вторую версию видно, что поименнованный список занимает меньше места, чем полноценный словарь,
даже с учетом того, что еще появляется фактически конкретный класс поименнованного списка, как лишний объект.
2. А вот очередь занимает в памяти больше места, чем список, что меня довольно удивило. Возможно это связано с их 
реализациями, для себя я еще проверю этот момент (к сожалению прямо сейчас нет времени при решении задачи).
3. Самым экономичным по памяти естественно стал вариант в котором отсутствует промежуточное хранение прибылей по 
кварталам. В данном варианте я переиспользовал один и тот же словарь, не плодя ненужных дополнительных конструкций.
4. В целом с точки зрения памяти коллекции, в случае поименнованного списка, являются хорошей заменой питоновскому 
словарю.
'''