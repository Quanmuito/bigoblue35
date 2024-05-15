# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/monks-business-day/
# Complexity: O(T * V * E). T for test cases, V for vertices, E for edges

INF = int(1e9) + 5

def BellmanFord():
    dist[1] = 0

    for i in range(1, N + 1): # i from 1 to N - 1: Run N - 1 times
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

                if i == N: # Run the Nth time, if dist still update -> positive cycle
                    return True

    return False

T = int(input())
for _ in range(T):
    N, M = map(int, input().strip().split(' '))
    graph = []
    dist = [INF for _ in range(N + 1)]

    for _ in range(M):
        i, j, C = map(int, input().strip().split(' '))
        graph.append((i, j, -C))

    print('Yes' if BellmanFord() else 'No')