def solve(n: int, b: int, queries: list):
    stack = []
    estimateDone = 0
    output = []

    while len(queries) > 0:
        moment, execute = queries.pop(0)

        while len(stack) > 0 and moment >= stack[0]:
            stack.pop(0)

        if len(stack) <= b:
            estimateDone = max(estimateDone, moment) + execute
            stack.append(estimateDone)
            output.append(estimateDone)
        else:
            output.append(-1)

    print(' '.join(list(map(str, output))))

    return

n, b = list(map(int, input().split(' ')))
queries = []
for i in range(n):
    t, d = list(map(int, input().split(' ')))
    queries.append((t, d))

solve(n, b, queries)