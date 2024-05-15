# https://vjudge.net/problem/HDU-1317
# Complexity: Bellman-Ford: O(V * E) -> BFS on each edges: O(E * (E + V))
# Total: O(T * V * E * (E + V)). T for test cases, V for vertices, E for edges

import queue

INF = int(1e9)

def BFS(start, end):
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        u = q.get()

        for v in BFSGraph[u]:
            if v == end: return True

            if not visited[v]:
                visited[v] = True
                q.put(v)

    return False

def BellmanFord(end):
    dist = [-INF for _ in range(n + 1)]
    dist[1] = 100

    for _ in range(n - 1):
        for u, v in graph:
            if dist[u] > 0:
                dist[v] = max(dist[v], dist[u] + energy[v])

    for u, v in graph:
        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and BFS(u, end):
            return True

    return dist[end] > 0

while True:
    n = int(input())
    if n == -1: break

    graph = []
    BFSGraph = [[] for _ in range(n + 1)]
    energy = [0 for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]
    for i in range(1, n + 1):
        data = list(map(int, input().split(' ')))
        energy[i] = data.pop(0)
        for j in range(data.pop(0)):
            graph.append((i, data[j]))
            BFSGraph[i].append(data[j])

    res = BellmanFord(n)
    print('winnable' if res else 'hopeless')