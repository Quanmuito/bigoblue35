from heapq import heappop, heappush

MAX = int(1e5)
INF = int(1e9)

def Dijkstra(start):
    dist = [INF for _ in range(MAX)]
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        w, u = heappop(pq)

        if w > dist[u]: continue

        for time, v in graph[u]:
            if w + time < dist[v]:
                dist[v] = w + time
                heappush(pq, (dist[v], v))

    return dist

N, M, k, x = map(int, input().strip().split(' '))
kCities = list(map(int, input().strip().split(' ')))

graph = [[] for _ in range(MAX)]
for _ in range(M):
    u, v, d = map(int, input().strip().split(' '))
    graph[u].append((d, v))
    graph[v].append((d, u))

A, B = map(int, input().strip().split(' '))
distA = Dijkstra(A)
distB = Dijkstra(B)

minTime = INF
for city in kCities:
    if distB[city] <= x: minTime = min(minTime, distA[city] + distB[city])

print(minTime if minTime != INF else -1)