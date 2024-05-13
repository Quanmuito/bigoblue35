from heapq import heappop, heappush

MAX = 105
INF = int(1e9)

def Dijkstra(start):
    dist = [INF for _ in range(MAX)]
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        w, u = heappop(pq)

        for time, v in graph[u]:
            if w + time < dist[v]:
                dist[v] = w + time
                heappush(pq, (dist[v], v))

    return dist

T = int(input())
for i in range(T):
    N = int(input())
    R = int(input())
    graph = [[] for _ in range(MAX)]

    for _ in range(R):
        u, v = map(int, input().strip().split(' '))
        graph[u].append((1, v))
        graph[v].append((1, u))

    s, d = map(int, input().strip().split(' '))
    distS = Dijkstra(s)
    distD = Dijkstra(d)

    totalTime = 0
    for j in range(N):
        totalTime = max(totalTime, distS[j] + distD[j])

    print(f"Case {i + 1}: {totalTime}")