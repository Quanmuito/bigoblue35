# Check up, down, left, right cell
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def atEdge(r, c): return r == 0 or c == 0 or r == R - 1 or c == C - 1

def DFS(start):
    stack = [start]
    visited[start[0]][start[1]] = True
    area = [start]
    connectedToEdge = False

    while len(stack) > 0:
        u = stack.pop()

        for i in range(4): # 4 adjection cells
            _r = u[0] + dr[i]
            _c = u[1] + dc[i]

            if _r in range(R) and _c in range(C) and graph[_r][_c] == '.' and not visited[_r][_c]:
                    if atEdge(_r, _c): connectedToEdge = True
                    visited[_r][_c] = True
                    area.append((_r, _c))
                    stack.append((_r, _c))
    return [] if connectedToEdge else area

R, C, K = map(int, input().split(' '))

visited = [[False] * C for _ in range(R)]
graph = []
for _ in range(R):
    sequence = input().strip()
    graph.append([char for char in sequence])

lakes = []
for r in range(R):
    for c in range(C):
        if graph[r][c] == '.' and not visited[r][c]:
            foundLake = DFS((r, c))
            if len(foundLake) > 0: lakes.append(foundLake)

sortedLakes = sorted(lakes, key = lambda arr: len(arr))

count  = 0
while len(sortedLakes) > K:
    lake = sortedLakes.pop(0)
    for r, c in lake:
        graph[r][c] = '*'
        count += 1

print(count)
for row in graph: print(''.join(row))

# Time Complexity: O(R * C + K)