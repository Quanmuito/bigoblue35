def solution(n: int, arr: list):
    totalA = totalB = 1
    timeA = timeB = 0

    timeA += arr[0]
    arr.pop(0)
    timeB += arr[-1]
    arr.pop()
    while len(arr) > 0:
        if timeA <= timeB:
            timeA += arr[0]
            arr.pop(0)
            totalA += 1
        else:
            timeB += arr[-1]
            arr.pop()
            totalB += 1

    print(totalA, totalB)
    return

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution(n, arr)

# Time Complexity: O(n)
# Space Complexity: O(1)