from heapq import heappush, heappop

MAX = 20005
INF = int(1e9)

def Dijkstra(start, graph):
    dist = [INF for _ in range(MAX)]
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        w, u = heappop(pq)

        if w > dist[u]: continue

        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                heappush(pq, (dist[v], v))
    return dist

N = int(input())
for i in range(1, N + 1):
    n, m, S, T = map(int, input().strip().split(' '))
    graph = [[] for _ in range(MAX)]


    for _ in range(m):
        u, v, w = map(int, input().strip().split(' '))
        graph[u].append((w, v))
        graph[v].append((w, u))

    dist = Dijkstra(S, graph)
    print(f"Case #{i}: {dist[T] if dist[T] != INF else 'unreachable'}")

