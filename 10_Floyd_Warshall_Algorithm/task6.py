# https://vjudge.net/problem/UVA-10803
# Complexity: O(T * (V^2 + V^3)). V is number of towns

INF = int(1e9) + 5
MAX = 102

def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

N = int(input())
for tc in range(1, N + 1):
    n = int(input())
    dist = [[0 if i == j else INF for i in range(n)] for j in range(n)]
    towns = []

    for i in range(n):
        x, y = map(int, input().split())
        towns.append((i, x, y))

    for i in range(n):
        id1, x1, y1 = towns[i]
        for j in range(i + 1, n):
            id2, x2, y2 = towns[j]
            w = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if w <= 10.0:
                dist[id1][id2] = w
                dist[id2][id1] = w

    FloydWarshall()

    print('Case #{}:'.format(tc))
    tc += 1

    maxDist = -1
    for i in range(n):
        for j in range(n):
            maxDist = max(maxDist, dist[i][j])

    print('{}'.format('Send Kurdy' if maxDist == INF else maxDist))
    print()