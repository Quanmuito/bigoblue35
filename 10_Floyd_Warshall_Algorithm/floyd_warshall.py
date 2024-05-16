INF = int(1e9) + 5

def printPath(path, start, end):
    if start == end: print(end)

    if path[start][end] == -1:
        print('No path')
        return

    printPath(path, start, path[start][end])
    print(end)

def printSolution(path, dist, V):
    for i in range(V):
        for j in range(V):
            if i != j:
                print('{} -> {}: '.format(i, j), end = '')
                printPath(path, i, j)
                print()

                if path[i][j] != -1:
                    print('Total length: {}'.format(dist[i][j]))


def FloydWarshall(graph, dist, path, V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and i != j: path[i][j] = i
            else: path[i][j] = -1

    for k in range(V):
        for i in range(V):
            if dist[i][k] == INF: continue

            for j in range(V):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    for i in range(V):
        if dist[i][i] < 0:
            return False
    return True

V = int(input())
graph = [[None for i in range(V)] for j in range(V)]
dist = [[None for i in range(V)] for j in range(V)]
path = [[None for i in range(V)] for j in range(V)]

for i in range(V):
    line = list(map(int, input().split()))
    for j in range(V):
        graph[i][j] = INF if line[j] == 0 and i != j else line[j]

    if FloydWarshall(graph, dist, path, V):
        printSolution(path, dist, V)
    else:
        print('Contain negative cycle')