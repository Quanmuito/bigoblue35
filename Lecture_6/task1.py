MAX = 1001
V = None
E = None

visited = [False] * MAX
dist = [0] * MAX
graph = [[] for _ in range(MAX)]

def DFS(start):
    stack = []
    stack.append(start)
    visited[start] = True

    while len(stack) > 0:
        u = stack.pop()

        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                dist[v] = dist[u] + 1

V = int(input())
E = V - 1
for _ in range(E):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

Q = int(input())
destinations = []
for _ in range(Q):
    destinations.append(int(input()))

start = 1
DFS(start)
id = 0
minDist = MAX

for end in destinations:
    if dist[end] < minDist or (dist[end] == minDist and end < id):
        minDist = dist[end]
        id = end

print(id)