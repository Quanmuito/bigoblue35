def DFS(start):
    count = 1
    stack = [start]
    visited[start] = True

    while len(stack) > 0:
        u = stack.pop()

        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                count += 1

    return count

V, E = map(int, input().split(' '))

graph = [[] for _ in range(V)]
for i in range(E):
    edge = input().strip()
    u, v = map(int, edge.split(' '))
    graph[u - 1].append(v - 1)

maxRange = 0
for k in range(V):
    visited = [False] * V
    maxRange = max(maxRange, DFS(k))

print(maxRange)