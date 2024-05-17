# https://vjudge.net/problem/UVA-423
INF = int(1e9)

n = int(input().strip())
MAX = n + 1

def BellmanFord():
    dist[1] = 0

    for _ in range(n):
        for u, v, w in graph:
            if dist[u] != INF:
                dist[v] = min(dist[v], dist[u] + w)

graph = []
dist = [INF for _ in range(MAX)]

for i in range(2, n + 1):
    data = input().split()

    for j in range(len(data)):
        w = data[j]
        if w != 'x':
            graph.append((i, j + 1, int(w)))
            graph.append((j + 1, i, int(w)))

BellmanFord()

maxDist = 0
for z in range(2, n + 1):
    if dist[z] != INF: maxDist = max(maxDist, dist[z])

print(maxDist)