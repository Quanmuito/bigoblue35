# https://codeforces.com/problemset/problem/295/B
# Complexity: O(N^3)

n = int(input())
MAX = n + 1

dist = [[0 for i in range(MAX)] for j in range(MAX)]
for i in range(1, MAX):
    a = list(map(int, input().split()))

    for j in range(1, MAX):
        dist[i][j] = a[j - 1]

removed = list(map(int, input().split()))
res = [0] * n

for index in range(n - 1, -1, -1):
    k = removed[index]

    for i in range(1, MAX):
        for j in range(1, MAX):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    total = 0
    for i in range(index, n):
        u = removed[i]
        for j in range(index, n):
            v = removed[j]
            total += dist[u][v]
    res[index] = total

for r in res:
    print(r, end=' ')