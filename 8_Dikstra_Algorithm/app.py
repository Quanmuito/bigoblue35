from heapq import heappop, heappush

MAX = 505
INF = int(1e9)

def Dijkstra(start, graph):
    dist = [INF for _ in range(MAX)]
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        w, u = heappop(pq)

        for length, v in graph[u]:
            if w + length < dist[v]:
                dist[v] = w + length
                heappush(pq, (dist[v], v))

    return dist

while True:
    N, M = map(int, input().strip().split(' '))

    if N == 0 and M == 0: break

    S, D = map(int, input().strip().split(' '))
    graphS = [[] for _ in range(MAX)]
    graphD = [[] for _ in range(MAX)]
    points = []

    for _ in range(M):
        U, V, P = map(int, input().strip().split(' '))
        graphS[U].append((P, V))
        graphD[V].append((P, U))
        points.append((U, V, P))

    distS = Dijkstra(S, graphS)
    distD = Dijkstra(D, graphD)
    newGraph = [[] for _ in range(MAX)]
    shortestPath = distS[D]

    if shortestPath == INF: print(-1)
    else:
        for U, V, P in points:
            if distS[U] + P + distD[V] != shortestPath:
                newGraph[U].append((P, V))

        newDist = Dijkstra(S, newGraph)
        print(newDist[D] if newDist[D] != INF else -1)