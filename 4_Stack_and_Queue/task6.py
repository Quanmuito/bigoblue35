def solve(n, t, queue: list):
    time = 0
    bank = 0
    output = {}

    while len(queue[0]) > 0 or len(queue[1]) > 0:
        firstArrival = 0
        if len(queue[0]) > 0 and len(queue[1]) > 0:
            firstArrival = min(queue[0][0][1], queue[1][0][1])
        else:
            if len(queue[0]) > 0:
                firstArrival = queue[0][0][1]
            if len(queue[1]) > 0:
                firstArrival = queue[1][0][1]

        time = max(time, firstArrival)
        load = 0

        while (len(queue[bank]) > 0 and load < n and queue[bank][0][1] <= time):
            index, _ = queue[bank].pop(0)
            output[index] = time + t
            load += 1
        time += t
        bank = 1 - bank

    keys = list(output.keys())
    keys.sort()

    for key in keys:
        print(output[key])
    return

nbrOfCase = int(input())
for i in range(nbrOfCase):
    n, t, m = list(map(int, input().split(' ')))
    queue = [[], []]
    for j in range(m):
        arrival, bank = input().split(' ')
        car = (j, int(arrival))
        if bank == 'left': queue[0].append(car)
        if bank == 'right': queue[1].append(car)

    solve(n, t, queue)
    if i < nbrOfCase - 1: print()