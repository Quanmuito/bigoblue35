def solution(points: list):
    listX = []
    listY = []

    for x, y in points:
        listX.append(x)
        listY.append(y)

    uniqueX = list(set(listX))
    uniqueY = list(set(listY))
    uniqueX.sort()
    uniqueY.sort()

    # x1, x2, x3 and y1, y2, y3
    if (len(uniqueX) != 3 or len(uniqueY) != 3):
        return 'ugly'

    sortedPoints = sorted(points)
    uniquePoints = []
    for x in uniqueX:
        for y in uniqueY:
            if x == uniqueX[1] and y == uniqueY[1]: continue
            else: uniquePoints.append((x, y))

    i = 0
    while i < 8:
        if sortedPoints[i] != uniquePoints[i]: return 'ugly'
        i += 1

    return 'respectable'

# Input
points = []
i = 0
while i < 8:
    points.append(tuple(map(int, input().split())))
    i += 1

# Output
print(solution(points))