import queue

MAX = 10005
INF = int(1e9)

class Node:
    def __init__(self, id, w):
        self.id = id
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

def dijkstra(start, end):
    dist = [INF for _ in range(MAX)]
    dist[start] = 0
    stack = queue.PriorityQueue()
    stack.put(Node(start, 0))

    while not stack.empty():
        top = stack.get()
        u = top.id
        w = top.w

        if id == end: break

        for neighbor in graph[u]:
            if w + neighbor.w < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.w
                stack.put(Node(neighbor.id, dist[neighbor.id]))

    return dist[end]

S = int(input())
for _ in range(S):
    N = int(input())
    cities = ['' for _ in range(10005)]
    graph = [[] for _ in range(MAX)]

    for i in range(N):
        cities[i + 1] = input()
        P = int(input())

        for j in range(P):
            nr, cost = map(int, input().split(' '))
            graph[i + 1].append(Node(nr, cost))

    R = int(input())
    for _ in range(R):
        startName, endName = input().split(' ')
        start = cities.index(startName)
        end = cities.index(endName)
        print(dijkstra(start, end))

    input()

# Optimize
from heapq import heappush, heappop

def Dijkstra(s, f):
	dist = [10 ** 9] * (N + 1)
	pq = [(0, s)]
	dist[s] = 0

	while pq:
		w, u = heappop(pq)

		if u == f:
			break

		for weight, v in graph[u]:
			if w + weight < dist[v]:
				dist[v] = w + weight
				heappush(pq, (dist[v], v))

	return dist[f]

T = int(input())

for t in range(T):
	N = int(input())
	graph = [[] for i in range(N + 1)]
	cities = []

	for u in range(1, N + 1):
		name = input()
		cities.append(name)
		neighbors = int(input())

		for i in range(neighbors):
			v, w = map(int, input().split())
			graph[u].append((w, v))

	Q = int(input())

	for i in range(Q):
		sCity, fCity = input().split()
		s = cities.index(sCity) + 1
		f = cities.index(fCity) + 1
		print(Dijkstra(s, f))

	input()
