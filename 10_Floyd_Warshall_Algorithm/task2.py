# https://vjudge.net/problem/UVA-10171
# Complexity: O(T * N^3)

MAX = 28
INF = int(1e9) + 5
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def FloydWarshall(dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    V = int(input())
    if V == 0: break

    distY = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    distM = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]

    for _ in range(V):
        age, direction, x, y, w = input().strip().split()

        u, v = map(ALPHABET.index, (x, y))
        w = int(w)

        if age == 'Y':
            distY[u][v] = min(distY[u][v], w)
            if direction == 'B':
                distY[v][u] = min(distY[v][u], w)
        else:
            distM[u][v] = min(distM[u][v], w)
            if direction == 'B':
                distM[v][u] = min(distM[v][u], w)

    FloydWarshall(distY)
    FloydWarshall(distM)

    S1, S2 = map(ALPHABET.index, input().strip().split())

    cost = INF
    res = []

    for i in range(MAX):
        dist1 = distY[S1][i]
        dist2 = distM[S2][i]

        if dist1 != INF and dist2 != INF and dist1 + dist2 <= cost:
            cost = dist1 + dist2
            res.append((dist1 + dist2, i))

    if not res:
        print('You will never meet.')
    else:
        res.sort()
        for place in res:
            if place[0] != cost: break
            print('{} {}'.format(cost, ALPHABET[place[1]]))

# Optimize
INF = 10 ** 9
MAX = 28

def FloydWarshall(dist):
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    N = int(input())
    if N == 0:
        break

    distS = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    distD = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]

    for _ in range(N):
        age, dir, x, y, c = input().split()
        u, v = map(lambda char: ord(char) - ord('A'), (x, y))
        c = int(c)

        if age == 'Y':
            distS[u][v] = min(distS[u][v], c)
            if dir == 'B':
                distS[v][u] = min(distS[v][u], c)
        else:
            distD[u][v] = min(distD[u][v], c)
            if dir == 'B':
                distD[v][u] = min(distD[v][u], c)

    s, d = map(lambda char: ord(char) - ord('A'), input().split())
    FloydWarshall(distS)
    FloydWarshall(distD)

    res = []
    minDist = INF

    for i in range(MAX):
        dist1 = distS[s][i]
        dist2 = distD[d][i]

        if dist1 != INF and dist2 != INF and dist1 + dist2 <= minDist:
            res.append((dist1 + dist2, i))
            minDist = dist1 + dist2

    if not res:
        print('You will never meet.')
    else:
        res.sort()
        print(minDist, end='')

        for place in res:
            if place[0] != minDist:
                break
            print(' ' + chr(place[1] + ord('A')), end = '')
        print()