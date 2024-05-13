from collections import deque

def solve(num: int, arr: list):
    q = deque()
    for i in range(num): q.append(i + 1)

    for command in arr:
        if command[0] == 'N':
            citizen = q.popleft()
            q.append(citizen)
            print(citizen)
        elif command[0] == 'E':
            citizen = int(command.split(' ')[1])
            if citizen in q: q.remove(citizen)
            q.insert(0, citizen)

    return

n = 1
while True:
    p, c = list(map(int, input().split(' ')))

    if p == 0 and c == 0: break

    arr = []
    for i in range(c):
        arr.append(input())

    print(f"Case {n}:")
    solve(min(p, c), arr)
    n += 1