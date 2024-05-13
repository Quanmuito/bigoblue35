MAX = 105
INF = int(1e9)

dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]
graph = []

def BellmanFord(start):
    dist[start] = 0

    for i in range(1, n):
        for j in range(m):
            u, v, w = graph[j]

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    for i in range(m):
        u, v, m = graph[i]
        if dist[u] != INF and dist[u] + w < dist[v]: return False

    return True

n, m = map(int, input().strip().split(' '))
for i in range(m):
    u, v, w = map(int, input().strip().split(' '))
    graph.append((u, v, w))

start, end = map(int, input().strip().split(' '))
BellmanFord(start)
print(dist[end])
