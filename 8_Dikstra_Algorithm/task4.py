from heapq import heappush, heappop

MAX = 10005
INF = int(1e9)

def Dijkstra(start, dist, graph):
	pq = [(0, start)]
	dist[start] = 0

	while pq:
		w, u = heappop(pq)

		if w > dist[u]: continue

		for weight, v in graph[u]:
			if w + weight < dist[v]:
				dist[v] = w + weight
				heappush(pq, (dist[v], v))

dataSets = int(input())
for _ in range(dataSets):
    N, M, K, S, T = map(int, input().split(' '))

    graphS = [[] for _ in range(MAX)]
    graphT = [[] for _ in range(MAX)]
    distT = [INF for _ in range(MAX)]
    distS = [INF for _ in range(MAX)]

    for _ in range(M):
        D, C, L = map(int, input().split(' '))
        graphS[D].append((L, C))
        graphT[C].append((L, D))

    Dijkstra(S, distS, graphS)
    Dijkstra(T, distT, graphT)
    shortest = distS[T]

    for _ in range(K):
        U, V, Q = map(int, input().split(' '))

        shortest = min(shortest, distS[U] + Q + distT[V], distS[V] + Q + distT[U])

    print(shortest if shortest != INF else -1)