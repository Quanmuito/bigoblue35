import queue

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(r, c):
    return r in range(R) and c in range(C)

def BFS(start):
    q = queue.Queue()
    q.put(start)
    visited[start[0]][start[1]] = True

    while not q.empty():
        u = q.get()

        for i in range(4):
            r = u[0] + dr[i]
            c = u[1] + dc[i]

            if isValid(r, c) and graph[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put((r, c))

while True:
    R, C = map(int, input().strip().split(' '))

    if R == 0 and C == 0: break

    graph = [['.'] * C for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    print(graph)
    bombRow = int(input().strip())
    for _ in range(bombRow):
        _input = list(map(int, input().strip().split(' ')))
        r = _input.pop(0)
        n = _input.pop(0)
        for c in _input:
            graph[r][c] = '*'

    start = tuple(map(int, input().strip().split(' ')))
    end = tuple(map(int, input().strip().split(' ')))

    for line in graph: print(line)