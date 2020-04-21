#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path) 

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
edges = [
	('A', 'C', 4),
	("A", "B", 1),
	("A", "D", 2),
	("B", "A", 9),
	("B", "E", 5),
	("C", "F", 15),
	("C", "A", 4),
	("D", "F", 7),
	("D", "A", 10),
	("E", "B", 3),
	("E", "J", 7),
	("J", "H", 2),
	("J", "I", 4),
	("H", "J", 13),
	("I", "G", 6),
	("G", "I", 4),
	("G", "F", 12),
	("F", "G", 9),
	("F", "K", 3),
	("K", "F", 6),
	("F", "D", 14),
	("F", "C", 11),
]
point_a=input('Введите начальную точку(A-J): ')
point_b=input('Введите конечную точку(либо ALL): ')
# Перебираем все вершины
i=0
tupl=[]
while len(edges) > i:
	tupl.append(edges[i][0])
	tupl.append(edges[i][1])
	i+=1
if point_b == 'ALL':
	for point_b in set(tupl):
		x,a=dijkstra(edges, point_b, point_a)
		print('Расстояние от точки {} до точки {}: {}\nПроходит через: {}'.format(point_a,point_b,x,a))
else:
	x,a=dijkstra(edges, point_b, point_a)
	print('Расстояние от точки {} до точки {}: {}\nПроходит через: {}'.format(point_a,point_b,x,a))

