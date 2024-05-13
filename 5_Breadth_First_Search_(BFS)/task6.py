from queue import Queue

# Check up, down, left, right cell
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def solve(frame, N, M):
    record = [0] * (M * N + 1)
    visited = [[False] * M for _ in range(N)]
    count = 0

    for row in range(N):
        for column in range(M):
            if visited[row][column]: continue
            if frame[row][column] == 1:
                start = (row, column)
                left = right = 0
                q = [None] * N * M
                q[0] = start
                visited[start[0]][start[1]] = True

                area = 1
                while left <= right:
                    u = q[left]
                    left += 1

                    for i in range(4): # 4 adjection cells
                        r = u[0] + dr[i]
                        c = u[1] + dc[i]

                        if r not in range(N) or c not in range(M): continue
                        if visited[r][c]: continue
                        visited[r][c] = True
                        if frame[r][c] == 1:
                            right += 1
                            q[right] = (r, c)
                            area += 1

                record[area] += 1
                count += 1

    print(count)
    for i in range(len(record)):
        if record[i] != 0: print(i, record[i])

    return

while True:
    N, M = list(map(int, input().split(' ')))

    if N == 0 and M == 0:
        break

    frame = []
    for _ in range(N):
        row = input().strip().split(' ')
        frame.append([int(cell) for cell in row])

    solve(frame, N, M)

# Loi giai

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

MAX = 251
table = [None] * MAX
slick = [0] * (MAX * MAX)
q = [None] * (MAX * MAX)

def BFS(sr, sc):
    left = right = 0
    q[0] = (sr, sc)
    table[sr][sc] = '0'
    count = 1

    while left <= right:
        ur, uc = q[left]
        left += 1

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(N) and c in range(M) and table[r][c] == '1':
                right += 1
                q[right] = (r, c)
                table[r][c] = '0'
                count += 1

    slick[count] += 1

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    for i in range(N):
        table[i] = input().split()
        for j in range(M):
            slick[i * M + j + 1] = 0

    nslicks = 0

    for i in range(N):
        for j in range(M):
            if table[i][j] == '1':
                nslicks += 1
                BFS(i, j)

    print(nslicks)

    for i in range(1, N * M  + 1):
        if slick[i]:
            print(i, slick[i], sep=' ')