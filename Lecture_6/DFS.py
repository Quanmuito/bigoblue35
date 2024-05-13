def DFS(start):
    stack = [start]
    visited[start] = True

    while len(stack) > 0:
        u = stack.pop()

        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                path[v] = u

def printPath(start, end):
    b = []
    if start == end:
        return 0

    if path[end] == -1:
        return -1

    while True:
        b.append(end)
        end = path[end]
        if start == end: break

V, E = map(int, input().split(' '))

path = [-1 for _ in range(V)]
visited = [False for _ in range(V)]
graph = [[] for _ in range(V)]
for i in range(E):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

start = 0
end = 5
DFS(start)
printPath(start, end)
