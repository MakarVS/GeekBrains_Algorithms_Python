# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Решите задачу при помощи построения графа.
from functools import reduce

n = int(input('Сколько встретилось друзей: '))
graph = [[int(i > j) for i in range(n)] for j in range(n)]
print(graph)
count = reduce(lambda acc, x: acc + sum(x), graph, 0)
print(f'Количество рукопожатий {count}')
