# https://www.spoj.com/problems/SOCIALNE/
# Complexity: O(T * V^3)

INF = int(1e9) + 5

def FloydWarshall():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

T = int(input().strip())
for tc in range(T):
    firstLine = input().strip()
    V = len(firstLine)
    matrix = [[*firstLine]]
    for i in range(V - 1):
        line = input().strip()
        matrix.append([*line])

    graph = [[INF for i in range(V)] for j in range(V)]
    dist = [[INF for i in range(V)] for j in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                graph[i][j] = 0
                dist[i][j] = 0

            if matrix[i][j] == 'Y':
                graph[i][j] = 1
                dist[i][j] = 1

    FloydWarshall()
    nfriends, index = 0, 0

    for i in range(V):
        count = 0

        for j in range(V):
            if dist[i][j] == 2:
                count += 1

        if count > nfriends:
            nfriends = count
            index = i

    print(index, nfriends)