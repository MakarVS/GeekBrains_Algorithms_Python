"""
Задача № 1.
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input('Введите кол-во друзей: '))

# Формирование матрицы смежности (фактически диагональ матрицы - 0), все остальное - 1
g = [[1 if i != j else 0 for i in range(n)] for j in range(n)]
print('Матрица смежности:')
print(*g, sep='\n')

edges_set = set()

# Фактически задача сводится к нахождению всех ребер графа
# В местах, где стоит единица - строим ребро из двух вершин, сортируем их и добавляем в множество для отбора уникальных
for id_1, line in enumerate(g):
    for id_2, el in enumerate(line):
        if el:
            edge = tuple(sorted((id_1, id_2)))
            edges_set.add(edge)

count = len(edges_set)
assert count == n * (n - 1) / 2, 'Не правильно найдено кол-во рукопожатий!'
print(f'Кол-во рукопожатий равно {count}')
