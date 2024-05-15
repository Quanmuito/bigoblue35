# https://www.spoj.com/problems/CHICAGO
# Complexity: O(T * V * E). T for test cases, V for vertices, E for edges

MAX = 105

def BellmanFord(start):
    dist[start] = 1.0

    for _ in range(n - 1):
        for u, v, w in graph:
            dist[u] = max(dist[u], dist[v] * w)
            dist[v] = max(dist[v], dist[u] * w)

while True:
    data = input().strip()
    if data == '0': break

    n, m = map(int, data.split())
    graph = []
    dist = [-1.0 for _ in range(MAX)]

    for _ in range(m):
        a, b, p = map(int, input().strip().split())
        graph.append((a, b, p / 100))

    BellmanFord(1)
    print("{:.6f} percent".format(dist[n] * 100))