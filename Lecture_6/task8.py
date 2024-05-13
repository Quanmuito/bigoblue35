def DFS(start, max_dist):
    dist = [-1] * (V + 1)
    stack = [start]
    dist[start] = 0

    while len(stack) > 0:
        u = stack.pop()

        for v, w in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                max_dist = max(max_dist, dist[v])
                stack.append(v)

    return (dist.index(max(dist)), max_dist)

T = int(input().strip())
for _ in range(T):
    V = int(input())
    E = V - 1
    graph = [[] for _ in range(V)]

    for i in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))

    leaf, max_dist = DFS(1, 0)
    _, output = DFS(leaf, max_dist)

    print(output)