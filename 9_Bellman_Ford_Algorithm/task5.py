# https://vjudge.net/problem/Kattis-shortestpath1
# Complexity: O(T * E * (V + E)). T for test cases, V for vertices, E for edges

import queue

MAX = 1005
INF = int(1e9) + 5

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

def BellmanFord(start):
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

while True:
    n, m, q, s = map(int, input().strip().split(' '))
    if n == 0 and m == 0 and q == 0 and s == 0: break
    graph = []
    BFSGraph = [[] for _ in range(MAX)]
    dist = [INF for _ in range(MAX)]

    for _ in range(m):
        u, v, w = map(int, input().strip().split(' '))
        graph.append((u, v, w))
        BFSGraph[u].append(v)
    BellmanFord(s)

    for _ in range(q):
        end = int(input().strip())
        if dist[end] == INF: print('Impossible')
        else:
            negative = False
            for u, v, w in graph:
                if dist[u] != INF and dist[u] + w < dist[v] and BFS(u, end):
                    negative = True
                    break
            print('-Infinity' if negative else dist[end])
    print()

# Optimize: Bellman-Ford: O(V * E), read output O(E + Q) => O(T * V * E)
INF = 10 ** 9

def BellmanFord(s):
    dist[s] = 0

    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

while True:
    n, m, q, s = map(int, input().split())

    if n == 0:
        break
    graph = []

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    dist = [INF] * n
    BellmanFord(s)

    for _ in range(q):
        f = int(input())

        if dist[f] == INF:
            print("Impossible")
        elif dist[f] == -INF:
            print("-Infinity")
        else:
            print(dist[f])
    print()