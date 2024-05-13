def solution(n, x, arr: list):

    arr.sort()
    minTime = 0

    for chapters in arr:
        minTime += chapters * x

        if x > 1: x -= 1

    print(minTime)

    return

# Input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Output
solution(n, x, arr)