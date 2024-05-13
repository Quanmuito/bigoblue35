from queue import Queue

# Check up, down, left, right cell
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def solve():
    visited = [[False] * M for _ in range(N)]

    q = Queue()
    q.put(start)
    visited[start[0]][start[1]] = True

    while not q.empty():
        u = q.get()

        for i in range(4): # 4 adjection cells
            r = u[0] + dr[i]
            c = u[1] + dc[i]

            if r == end[0] and c == end[1] and frame[r][c] == 'X': return 'YES'

            if r in range(N) and c in range(M) and frame[r][c] == '.':
                frame[r][c] = 'X'
                q.put((r, c))

    return 'NO'

N, M = list(map(int, input().split(' ')))

frame = []
for _ in range(N):
    row = input()
    frame.append([char for char in row])

start = tuple(map(lambda x: int(x) - 1, input().split(' ')))
end = tuple(map(lambda x: int(x) - 1, input().split(' ')))

print(solve())