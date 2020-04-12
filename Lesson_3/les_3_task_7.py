# Задача № 7.
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

lst = [random.randint(-10, 10) for i in range(1, 10)]
print(f'Исходные массив {lst}')

m_1 = lst[0]
m_2 = lst[1]

for i in range(2, len(lst)):
    if i % 2 == 0:
        if lst[i] < m_1:
            m_1 = lst[i]
        elif lst[i] < m_2:
            m_2 = lst[i]

        if m_2 < m_1:
            m_1, m_2 = m_2, m_1
    else:
        if lst[i] < m_2:
            m_2 = lst[i]
        elif lst[i] < m_1:
            m_1 = lst[i]

        if m_1 < m_2:
            m_1, m_2 = m_2, m_1


print(f'Первый наименьший элемент: {m_1}')
print(f'Второй наименьший элемент: {m_2}')
