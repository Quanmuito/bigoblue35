import queue

MAX = 105
INF = int(1e9) + 7
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]

class Cell:
    def __init__(self, id, w):
        self.id = id
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

def dijkstra(start):
    stack = queue.PriorityQueue()
    stack.put(Cell(start, 0))
    dist[start] = 0

    while not stack.empty():
        top = stack.get()
        u = top.id
        w = top.w

        for neighbor in graph[u]:
            if w + neighbor.w < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.w
                stack.put(Cell(neighbor.id, dist[neighbor.id]))

N = int(input())
E = int(input())
T = int(input())

M = int(input())
for _ in range(M):
    A, B, W = map(int, input().split(' '))
    graph[B].append(Cell(A, W))

dijkstra(E)

count = 0
for i in range(1, N + 1):
    if dist[i] <= T: count += 1
print(count)