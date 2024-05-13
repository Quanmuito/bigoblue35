# Move around
dr = [1, 1, 0, -1, -1, -1, 0, 1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def DFS(start):
    target = [char for char in 'ALLIZZWELL']
    position = 1
    visited = [[False] * C for _ in range(R)]

    stack = [start]
    visited[start[0]][start[1]] = True

    while len(stack) > 0:
        u = stack.pop(0)

        for i in range(8): # 4 adjection cells
            _r = u[0] + dr[i]
            _c = u[1] + dc[i]

            if _r in range(R) and _c in range(C) and not visited[_r][_c] and graph[_r][_c] == target[position]:
                visited[_r][_c] = True
                stack.append((_r, _c))
                position += 1
                if position == len(target): return True
                break

    return False

T = int(input())

for _ in range(T):
    _input = input().strip()
    R, C = map(int, _input.split(' '))

    graph = []
    for _ in range(R):
        _input = input().strip()
        graph.append([char for char in _input])

    starts = []
    for r in range(R):
        for c in range (C):
            if graph[r][c] == 'A':
                starts.append((r, c))

    output = False
    for start in starts:
        output = DFS(start)
        if output:
            output = True
            break

    print('YES' if output else 'NO')
    input()

# Optimize

import sys
sys.setrecursionlimit(100000)

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]
term = "ALLIZZWELL"

def DFS(sr, sc, count):
    global found, table, visited
    if count == len(term):
        found = True
        return

    for i in range(8):
        r = sr + dr[i]
        c = sc + dc[i]

        if r in range(R) and c in range(C) and table[r][c] == term[count] and not visited[r][c]:
            visited[r][c] = True
            DFS(r, c, count + 1)
            visited[r][c] = False

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    table = []
    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        table.append(input())

    found = False

    for i in range(R):
        for j in range(C):
            if table[i][j] == term[0] and not found:
                DFS(i, j, 1)

    print("YES" if found else "NO")