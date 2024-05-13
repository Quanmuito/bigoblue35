from queue import Queue

# Check up, down, left, right cell
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c

def findInAndOut(maze: list):
    IO = []
    # Find at row 0
    if '.' in maze[0]:
        for i in range(len(maze[0])):
            if maze[0][i] == '.': IO.append(Cell(0, i))

    # Find at last row
    if len(maze) > 1 and '.' in maze[-1]:
        for i in range(len(maze[-1])):
            if maze[-1][i] == '.': IO.append(Cell(len(maze) - 1, i))

    # Find at egde (first and last element of each row)
    i = 1
    while i < len(maze) - 1:
        if maze[i][0] == '.': IO.append(Cell(i, 0))
        if len(maze[i]) > 1 and maze[i][-1] == '.': IO.append(Cell(i, len(maze[i]) -1))
        i += 1

    return IO

def solve(maze: list, visited: list, m, n):
    IO = findInAndOut(maze)
    if len(IO) != 2: return False

    start, end = IO
    q = Queue()
    q.put(start)
    visited[start.r][start.c] = True

    while not q.empty():
        u = q.get()

        if u.r == end.r and u.c == end.c:
            return True

        for i in range(4): # 4 adjection cells
            r = u.r + dr[i]
            c = u.c + dc[i]

            if r in range(m) and c in range(n) and not visited[r][c] and maze[r][c] == '.':
                visited[r][c] = True
                q.put(Cell(r, c))

    return False

t = int(input())

for _ in range(t):
    m, n = list(map(int, input().split(' ')))

    maze = []
    vistited = []
    for row in range(m):
        content = input()
        maze.append([char for char in content])
        vistited.append([False for _ in content])

    print('valid' if solve(maze, vistited, m, n) else 'invalid')