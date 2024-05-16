# https://www.codechef.com/practice/course/dynamic-programming/INTDP01/problems/MAXCOMP
# Complexity: O(T * N^3)

INF = int(1e9) + 5
MAX = 49

def FloydWarshall():
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                if i <= k <= j:
                    dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())
for _ in range(T):
    N = int(input())
    dist = [[0 for i in range(MAX)] for j in range(MAX)]

    for _ in range(N):
        S, E, C = map(int, input().split())
        dist[S][E] = max(dist[S][E], C)

    FloydWarshall()

    print(dist[0][MAX - 1])