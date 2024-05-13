dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]
term = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def DFS(start):
    position = 0
    stack = [start]

    while len(stack) > 0:
        u = stack.pop(0)

        if graph[u[0]][u[1]] == term[position]: position += 1
        if position == len(term): break

        for i in range(8): # 8 adjection cells
            _r = u[0] + dr[i]
            _c = u[1] + dc[i]

            if _r in range(R) and _c in range(C) and graph[_r][_c] == term[position]:
                stack.append((_r, _c))

    return position

case = 1
while True:
    _input = input().strip()
    R, C = map(int, _input.split())

    if R == 0 and C == 0: break

    graph = []
    for i in range(R):
        _input = input().strip()
        graph.append([char for char in _input])

    maxRange = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] == term[0]:
                maxRange = max(maxRange, DFS((i, j)))

    print(f"Case {case}: {maxRange}")
    case += 1