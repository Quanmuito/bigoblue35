from queue import Queue

def checkPath(dist: list, path: list, start: int, end: int, m: int):
    if path[end] == -1:
        return 0

    while True:
        if dist[end] > m: return 0
        end = path[end]
        if end == start: return 1

def solve(graph, map, n, m):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    count = 0

    q = Queue()
    q.put(1)
    visited[1] = True
    dist[1] = map[0]

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True

                if map[v - 1] == 1:
                    dist[v] = dist[u] + 1

                if dist[v] <= m:
                    if len(graph[v]) == 1:
                        count += 1
                    else:
                        q.put(v)

    print(count)

    return

n, m = list(map(int, input().split(' ')))
map = list(map(int, input().split(' ')))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2 = input().split(' ')
    graph[int(v1)].append(int(v2))
    graph[int(v2)].append(int(v1))

solve(graph, map, n, m)