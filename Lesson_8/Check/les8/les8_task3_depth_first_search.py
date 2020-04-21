'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

import random

def ft_graph_fill(n):
    graph = []
    for i in range(n):
        ##granting at least one connection for every node to the previous one
        if (i > 0) and (n != 2):
            a = [x for x in graph[i - 1] if x != i]
            print(a)
            conn = [random.choice(a)]
        else:
            conn = []
        graph.append(conn)
        ##finding possible connections without repeats and loops to current node
        arr = [x for x in range(n) if x != i and x not in conn]
        ##generating random quantity of nodes connected to current node
        ##should not be more than quantity of possible connections
        if (len(arr) > 1):
            k = random.choice(range(1, len(arr)))
        else:
            k = 1
        for j in range(k):
            num = random.choice(arr)
            while (num in graph[i]):
                num = random.choice(arr)
            graph[i].append(num)
    return (graph)

def ft_print_graph(graph):
    for i in range(len(graph)):
        print(str(i) + "->" + "->".join(["%d"] * len(graph[i])) % tuple(sorted(graph[i])))

def ft_depth_first_search(visited, graph, current, res):
    if current not in visited:
        res.append(current)
        visited.add(current)
        for node in graph[current]:
            ft_depth_first_search(visited, graph, node, res)

n = int(input("Put nodes quantity: "))
graph = ft_graph_fill(n)
print("Generated graph: ")
ft_print_graph(graph)
current = int(input("Put the starting node number to build the way (0..{}): ".format(n - 1)))
visited = set()
res = []
ft_depth_first_search(visited, graph, current, res)
print("Resulting way: " + "->".join(["%d"] * len(res)) % tuple(res))
