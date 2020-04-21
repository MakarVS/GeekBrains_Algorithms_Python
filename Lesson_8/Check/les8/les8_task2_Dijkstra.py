'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''
graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def ft_dijkstra(graph, start):
    length = len(graph)
    save_start = start
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [start] * length
    cost[start] = 0
    min_cost = 0
    while (min_cost < float('inf')):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if (vertex != 0) and not (is_visited[i]):
                if (cost[i] > vertex + cost[start]):
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if (min_cost > cost[i]) and not (is_visited[i]):
                min_cost = cost[i]
                start = i
    way = []
    for i in range(len(cost)):
        way.append([save_start])
        n = i
        tmp = []
        while (parent[n] != save_start):
            tmp.append(parent[n])
            n = parent[n]
        way[i] += tmp[::-1]
        way[i].append(i)
    for i in range(len(cost)):
        if (cost[i] != float('inf')):
            print("Cost of moving " + "->".join(["%d"] * len(way[i])) % tuple(way[i]) + " is {}".format(cost[i]))
        else:
            print("No way for " + "->".join(["%d"] * len(way[i])) % tuple(way[i]))

n = int(input("Put starting vertex (0..7): "))
ft_dijkstra(graph, n)
