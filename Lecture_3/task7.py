def solution(k: int, arr: list):
    arr.sort()
    arr.reverse()

    i = 0
    length = 0
    while i < 12:
        if length < k: length += arr[i]
        else: break

        i += 1

    print(i if i >= 0 else -1)

    return

# Input
k = int(input())
arr = list(map(int, input().split()))

# Output
solution(k, arr)