import queue
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

MAX = 500 + 1
backyard = [None] * MAX
nsheeps = nwolves = 0

def BFS(sr, sc):
    global nsheeps, nwolves
    q = queue.Queue()
    q.put((sr, sc))

    sheep = (1 if backyard[sr][sc] == 'k' else 0)
    wolf = (1 if backyard[sr][sc] == 'v' else 0)

    canEscape = False
    backyard[sr][sc] = '#'

    while not q.empty():
        ur, uc = q.get()

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if not (r in range(N) and c in range(M)):
                canEscape = True
                continue

            if backyard[r][c] != '#':
                sheep += (1 if backyard[r][c] == 'k' else 0)
                wolf += (1 if backyard[r][c] == 'v' else 0)
                backyard[r][c] = '#'
                q.put((r, c))

    if canEscape:
        nsheeps += sheep
        nwolves += wolf
    else:
        if sheep > wolf:
            nsheeps += sheep
        else:
            nwolves += wolf

line = ''
while line == '':
    line = input().strip()

N, M = map(int, line.split())

for i in range(N):
    backyard[i] = list(input())

for i in range(N):
    for j in range(M):
        if backyard[i][j] != '#':
            BFS(i, j)

print(nsheeps, nwolves)