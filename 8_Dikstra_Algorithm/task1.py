import queue

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def dijkstra(start):
    stack = queue.PriorityQueue()
    stack.put(Node(start, 0))
    dist[start] = 0

    while stack.empty() == False:
        top = stack.get()
        u = top.id
        w = top.dist

        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                stack.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u
    return

MAX = 505
N = int(input())
graph = [[] for _ in range(MAX)]
dist = [float('inf') for _ in range(MAX)]
path = [-1 for _ in range(MAX)]

for _ in range(N):
    A, B, W = map(int, input().split(' '))
    graph[A].append(Node(B, W))
    graph[B].append(Node(A, W))

start = int(input())
dijkstra(start)

Q = int(input())
for _ in range(Q):
    end = int(input())
    print(dist[end] if dist[end] != float('inf') else 'NO PATH')