# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=508

INF = int(1e9) + 5
MAX = 21

def FloydWarshall():
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

tc = 1
while True:
    try:
        dist = [[0 if i == j else INF for i in range(MAX)] for j in range(MAX)]

        for i in range(1, 20):
            data = list(map(int, input().strip().split()))
            if len(data) > 0: data.pop(0)

            for country in data:
                dist[i][country] = 1
                dist[country][i] = 1

        FloydWarshall()

        q = int(input())
        print('Test Set #{}'.format(tc))
        for _ in range(q):
            start, end = map(int, input().strip().split())
            print('{} to {}: {}'.format(start, end, dist[start][end]))

        print()
        tc += 1
    except EOFError:
        break

# Submitable version
N = 20
t = 1

def FloydWarshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    try:
        dist = [[10 ** 9] * (N + 1) for _ in range(N + 1)]
        for i in range(1, N):
            for j in list(map(int, input().split()))[1:]:
                dist[i][j] = dist[j][i] = 1

        FloydWarshall()

        print("Test Set #{}".format(t))
        t += 1

        Q = int(input())
        for _ in range(Q):
            u, v = map(int, input().split())
            print('{:2d} to {:2d}: {}'.format(u, v, dist[u][v]))
        print()

    except EOFError:
        break