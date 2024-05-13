from queue import Queue

# Check up, down, left, right cell
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c

def solve(map, visited, W, H):
    q = Queue()

    for r in range(H):
        for c in range(W):
            if map[r][c] == '@':
                q.put(Cell(r, c))
                visited[r][c] = True
                break

    while not q.empty():
        u = q.get()

        for i in range(4): # 4 adjection cells
            r = u.r + dr[i]
            c = u.c + dc[i]

            if r in range(H) and c in range(W) and not visited[r][c] and map[r][c] == '.':
                visited[r][c] = True
                q.put(Cell(r, c))

    count = 0
    for r in range(H):
        for c in range(W):
            if visited[r][c]: count += 1
    return count


T = int(input())
for t in range(T):
    withHeight = input().split(' ')

    map = []
    visited = []
    for row in range(int(withHeight[1])):
        content = input()
        map.append([char for char in content])
        visited.append([False for _ in content])

    print(f"Case {t + 1}: {solve(map, visited, int(withHeight[0]), int(withHeight[1]))}")
