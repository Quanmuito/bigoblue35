def solution(n: int, arr: list):
    unique = list(set(arr))
    unique.sort()
    count = {}

    for x in unique:
        count[x] = arr.count(x)

    maxHeight = 1
    for _, number in count.items():
        maxHeight = max(maxHeight, number)

    print(maxHeight, len(unique))

    return

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution(n, arr)