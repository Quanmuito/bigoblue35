# https://lightoj.com/problem/extended-traffic
# Complexity: O(T * V * E). T for test cases, V for vertices, E for edges

MAX = 205
INF = int(1e9)

def BellmanFord(start):
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]: dist[v] = dist[u] + w

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]: dist[v] = -INF

T = int(input())
for i in range(T):
    input()
    n = int(input())
    busy = list(map(int, input().strip().split(' ')))

    graph = []
    dist = [INF for _ in range(MAX)]
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split(' '))
        w = (busy[v - 1] - busy[u - 1]) ** 3
        graph.append((u, v, w))
    BellmanFord(1)

    print(f"Case {i + 1}:")
    q = int(input())
    for _ in range(q):
        end = int(input())
        print(dist[end] if (dist[end] != INF and dist[end] >= 3) else '?')