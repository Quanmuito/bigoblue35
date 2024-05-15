# https://www.spoj.com/problems/UCV2013B/
# Complexity: O(T * Q * N * M)

INF = int(1e9) + 5

def BellmanFord(start, n):
    dist = [INF for _ in range(n)]
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            dist[v] = min(dist[v], dist[u] + w)

    for u, v, w in graph:
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = -INF

    return dist

count = 1
while True:
    N = int(input())
    if N == 0: break
    names = []
    graph = []

    for i in range(N):
        data = input().strip().split(' ')
        names.append(data.pop(0))
        for j in range(N):
            w = int(data[j])
            if i != j and w == 0:
                continue
            if i == j and w >= 0:
                w = 0
            graph.append((i, j, w))

    Q = int(input())
    print("Case #{}:".format(count))
    for _ in range(Q):
        start, end = map(int, input().strip().split(' '))
        dist = BellmanFord(start, N)
        if dist[end] == -INF: print('NEGATIVE CYCLE')
        else: print("{}-{} {}".format(names[start], names[end], 'NOT REACHABLE' if dist[end] == INF else dist[end]))
    count += 1

# Optimize: O(T * N^2 * M)
INF = 100 * (1 << 30) + 7     # Should be large enough

def BellmanFord(s):
    dist[s][s] = 0

    for _ in range(n - 1):
        for edge in graph:
            u, v, w = edge
            if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                dist[s][v] = dist[s][u] + w

    for _ in range(n - 1):
        for edge in graph:
            u, v, w = edge
            if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                dist[s][v] = -INF

tc = 1
while True:
    n = int(input())
    if n == 0:
        break

    monuments = []
    graph = []
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        name, *weights = input().split()
        monuments.append(name)
        for j in range(n):
            w = int(weights[j])
            if i != j and w == 0:
                continue
            if i == j and w >= 0:
                w = 0
            graph.append((i, j, w))

    for i in range(n):
        BellmanFord(i)

    print('Case #{}:'.format(tc))
    tc += 1
    q = int(input())

    for _ in range(q):
        u, v = map(int, input().split())
        if dist[u][v] <= -INF:
            print('NEGATIVE CYCLE')
        else:
            print('{}-{} {}'.format(monuments[u], monuments[v], 'NOT REACHABLE' if dist[u][v] == INF else dist[u][v]))