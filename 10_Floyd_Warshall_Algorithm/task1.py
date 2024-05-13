MAX = 1005
INF = int(1e9)

def BellmanFord(start, n, m):
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != INF and dist[u] + w < dist[v]: return False

    return True

c = int(input().strip())
for _ in range(c):
    n, m = map(int, input().strip().split(' '))
    graph = []
    dist = [INF for _ in range(MAX)]

    for _ in range(m):
        wormhole = tuple(map(int, input().strip().split(' ')))
        graph.append(wormhole)

    res = BellmanFord(0, n, m)
    print('possible' if not res else 'not possible')