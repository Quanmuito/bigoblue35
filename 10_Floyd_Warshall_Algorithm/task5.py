# https://vjudge.net/problem/UVA-10246
# Complexity: O(T * C^3)

MAX = 81
INF = int(1e9) + 5

def FloydWarshall():
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                maxFeast = max(maxCost[i][k], maxCost[k][j])
                if dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    maxCost[i][j] = maxFeast

tc = 1
while True:
    C, R, Q = map(int, input().split())
    if C == 0 and R == 0 and Q == 0: break

    cost = [0] + list(map(int, input().split()))
    maxCost = [[0 if i == j else INF for i in range(MAX)] for j in range(MAX)]
    for i in range(C + 1):
        for j in range(C + 1):
            maxCost[i][j] = max(cost[i], cost[j])

    dist = [[0 if i == j else INF for i in range(MAX)] for j in range(MAX)]
    for _ in range(R):
        c1, c2, d = map(int, input().split())
        dist[c1][c2] = d
        dist[c2][c1] = d

    FloydWarshall()
    FloydWarshall()

    print('Case #{}'.format(tc))
    tc += 1

    for _ in range(Q):
        start, end = map(int, input().split())
        print(-1 if dist[start][end] == INF else dist[start][end] + maxCost[start][end])

    print()