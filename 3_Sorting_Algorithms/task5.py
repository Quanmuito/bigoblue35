def solution(n: int, w: int, arr: list):
    arr.sort()
    xMaxForGirl = arr[0]
    xMaxForBoy = arr[n] / 2
    xMax = w / (3 * n)

    x = min(xMax, xMaxForGirl, xMaxForBoy)
    print(3 * x * n)

    return

# Input
n, w = list(map(int, input().split()))
arr = list(map(int, input().split()))

# Output
solution(n, w, arr)