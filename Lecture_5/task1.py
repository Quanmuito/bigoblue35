from queue import Queue

def BFS(graph, V, start: int):
    visited = [False for _ in range(V + 1)]
    path = [-1 for _ in range(V + 1)]

    q = Queue()
    visited[start] = True
    q.put(start)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
    return path

def printPath(path: list, start: int, end: int):
    if path[end] == -1:
        return -1

    b = []
    while True:
        b.append(end)
        end = path[end]
        if end == start: return len(b)

q = int(input())
for i in range(q):
    V, E = list(map(int, input().split(' ')))
    vertices = [v + 1 for v in range(V)]

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = list(map(int, input().split(' ')))
        graph[v1].append(v2)
        graph[v2].append(v1)

    start = int(input())
    path = BFS(graph, V, start)

    output = []
    for v in vertices:
        if v == start: continue
        distance = printPath(path, start, v)
        if distance == -1: output.append(-1)
        else: output.append(distance * 6)

    print(' '.join(list(map(str, output))))
