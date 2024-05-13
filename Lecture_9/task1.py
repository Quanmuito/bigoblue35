def solve():
    stack = [(A[i], i) for i in range(N)]

    time = 0
    while len(stack) > 0:
        highestPrior = max(stack)
        firstJob = stack.pop(0)

        if highestPrior[0] == firstJob[0]:
            time += 1
            if firstJob[1] == M: return time

        else: stack.append(firstJob)

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().strip().split(' '))
    A = list(map(int, input().strip().split(' ')))
    print(solve())