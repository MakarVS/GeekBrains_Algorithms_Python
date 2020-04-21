"""
Задача № 2.
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    _start = start

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    way = [deque() for _ in range(length)]
    for i in range(length):
        j = i
        while parent[j] != _start:
            if parent[j] != -1:
                way[i].appendleft(str(parent[j]))
            else:
                break
            j = parent[j]
        else:
            way[i].appendleft(str(_start))
            way[i].append(str(i))

        if i == _start:
            way[i].appendleft(str(i))

    return cost, way


s = int(input('От какой вершины идти? '))
cost, way = dijkstra(g, s)

for i in range(len(cost)):
    length = len(way[i])
    if length > 1:
        print(f'Кратчайшее расстояние от вершины {s} до вершины {i} равно {cost[i]} при этом надо пройти через вершины:'
              f' {", ".join(list(way[i]))}')
    elif i == s:
        print(f'{i} - начальная вершина')
    else:
        print(f'Из вершины {s} в вершину {i} нет пути')
