# https://basecamp.eolymp.com/en/problems/1108
# Complexity: O(T * V * E). T for test cases, V for vertices, E for edges

MAX = 1005
INF = int(1e9)

def BellmanFord(start, n):
    dist[start] = 0

    for i in range(n): # i run from 0 -> n - 2: n - 1 times
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if i == n - 1: # Run the Nth time, if dist still update -> negative cycle
                    return True

    return False

c = int(input().strip())
for _ in range(c):
    n, m = map(int, input().strip().split(' '))
    graph = []
    dist = [INF for _ in range(MAX)]

    for _ in range(m):
        wormhole = tuple(map(int, input().strip().split(' ')))
        graph.append(wormhole)

    res = BellmanFord(0, n)
    print('possible' if res else 'not possible')