'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

def flatten(mat):
    return [x for arr in mat for x in arr]

n = int(input("Put friends quantity: "))
graph = []
while (n > 0):
    shakes = [x for x in range(1, n)]
    if (len(shakes) > 0):
        graph.append(shakes)
    n -= 1
print(graph)
for i in range(len(graph)):
    print("Friend #{} shaked hands with ".format(len(graph) + 1 - i))
    print(*graph[i], sep=", ")
print('*' * 50)
print("Total handshakes quantity is {}".format(len(flatten(graph))))
