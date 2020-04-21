"""
Задача № 3.
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
from random import randint

# !!!!!!!!!ВНИМАНИЕ!!!!!!!!!
# Заккоментированные строки позволяют визуализировать сгенерированный граф, для этого требуется установить 2 библиотеки:
# networkx и matplotlib

# import networkx as nx
# import matplotlib.pyplot as plt


def gener_graph(n):
    """
    Функция для рандомной генерации графа
    :param n: кол-во вершин
    :return: граф смежности
    """
    graph = {}
    for i in range(n):
        line = set()
        list_vert = list(range(n))
        list_vert.remove(i)
        vert = randint(1, n - 1)
        for _ in range(vert):
            r = randint(0, len(list_vert)-1)
            line.add(list_vert.pop(r))
        graph[i] = line

    return graph


# def graph_viz(graph):
#     """
#     Визуализация графа для проверки (все ли вершины связаны, нет ли петель)
#     :param graph: граф смежности
#     :return:
#     """
#     G = nx.DiGraph(graph)
#     labels = {i: str(i) for i in graph}
#     nx.draw(G, pos=nx.spring_layout(G), labels=labels)
#     plt.show()


def depth_first_search(graph, start):
    """
    Алгоритм обхода графа в глубину
    :param graph: граф смежности
    :param start: исходная вершина
    :return: список для построения путей из вершины start до всех доступных вершин
    """
    def func_buf(start, is_visited, prev, g):
        is_visited[start] = True
        for u in g[start]:
            if not is_visited[u]:
                prev[u] = start
                func_buf(u, is_visited, prev, graph)

    n = len(graph)
    is_visited = [False] * n
    prev = [None] * n

    func_buf(start, is_visited, prev, graph)
    return prev


n_edges = int(input('Введите кол-во вершин: '))
graph = gener_graph(n_edges)
print(f'Сгенерированный граф в виде списка смежностей:\n{graph}')
# graph_viz(graph)
vertex = int(input('Из какой вершины делать обход? '))
print(f'Результат обхода графа:\n {depth_first_search(graph, vertex)}')
