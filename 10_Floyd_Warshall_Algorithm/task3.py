# https://vjudge.net/problem/UVA-104
# Complexity: O(T * N^3)

def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

    for i in range(n):
        if dist[i][i] > 1:
            return True

    return False

tc = 1
while True:
    n = int(input())
    if n == 0: break

    dist = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    names = []
    for _ in range(n):
        names.append(input().strip())

    m = int(input())
    for _ in range(m):
        cur1, rate, cur2 = input().strip().split()

        u, v = map(lambda x: names.index(x), (cur1, cur2))
        dist[u][v] = float(rate)
    input()

    print('Case {}: {}'.format(tc, 'Yes' if FloydWarshall() else 'No'))
    tc += 1