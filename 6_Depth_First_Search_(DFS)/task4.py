import sys
visited = [False] * 10005
graph = [[] for _ in range(10005)]

sys.setrecursionlimit(10005)
def DFS(u):
    visited[u] = 1

    for v in graph[u]:
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if DFS(v):
                return True

    visited[u] = 2
    return False

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    for i in range(N + 1):
        graph[i].clear()
        visited[i] = 0

    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)

    isCyclic = False

    for i in range(1, N + 1):
        if visited[i] == 0:
            isCyclic = DFS(i)
            if isCyclic:
                break

    print("YES" if isCyclic else "NO")