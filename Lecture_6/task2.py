def DFS(start):
    stack = [start]
    visited[start] = True

    while len(stack) > 0:
        u = stack.pop()

        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True

T = int(input())
for _ in range(T):
    V = int(input())
    visited = [False for _ in range(V)]
    graph = [[] for _ in range(V)]

    E = int(input())
    for _ in range(E):
        u, v = map(int, input().split(' '))
        graph[u].append(v)
        graph[v].append(u)

    meet = 0
    for student in range(V):
        if not visited[student]:
            DFS(student)
            meet += 1

    print(meet)