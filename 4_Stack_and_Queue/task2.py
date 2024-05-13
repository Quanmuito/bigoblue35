def solve(t: int, arr: list):
    main = [1]
    side = []

    for x in arr:
        while len(side) > 0:
            if side[-1] == main[-1] + 1:
                main.append(side.pop())
            else: break

        if x == 1: continue
        elif x == main[-1] + 1: main.append(x)
        else: side.append(x)

    while len(side) > 0:
        if side[-1] == main[-1] + 1:
            main.append(side.pop())
        else: break

    return 'yes' if len(side) == 0 else 'no'

# Input
test = []
while True:
    value = input()
    if (value == '0'):
        break
    test.append(value)

# Output
i = 0
while i < len(test):
    print(solve(test[i], list(map(int, test[i + 1].split(' ')))))
    i += 2
