"""
Задача № 2.
Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, OrderedDict
from heapq import heappush, heappop


class MyNode:

    def __init__(self, data=None, flag_leaf=True, left=None, right=None):
        self.flag_leaf = flag_leaf

        if flag_leaf:
            self.data = data
        else:
            self.left = left
            self.right = right

    def search(self, code_dict, code):
        if self.flag_leaf:
            code_dict[self.data] = code or '0'
        else:
            self.left.search(code_dict, code+'0')
            self.right.search(code_dict, code+'1')


def huffman_encode(s):
    freq_dict = Counter(s)
    l = []
    count = 0

    for let in freq_dict:
        heappush(l, (freq_dict[let], count, MyNode(data=let)))
        count += 1

    while len(l) > 1:
        wieght_1, _, left = heappop(l)
        wieght_2, _, right = heappop(l)
        heappush(l, (wieght_1 + wieght_2, count, MyNode(flag_leaf=False, left=left, right=right)))
        count += 1

    code_dict = {}

    if l:
        root = l[0][2]
        root.search(code_dict, '')

    return code_dict


s = input('Введите строку: ')

code_dict = huffman_encode(s)

print('Таблица кодировки:')
for key, value in code_dict.items():
    print(f'"{key}" - {value}')

print('Закодированная строка:')
print(''.join([code_dict[let]+' ' for let in s]))
