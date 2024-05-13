def solution(n, arr: list):
    if n == 1:
        print('yes')
        print(1, 1)
        return

    l = r = 0
    reversed = False if arr[0] < arr[1] else True

    i = 1
    while i < n:
        if not reversed and arr[i] < arr[i - 1]:
            l = i - 1
            r = i
            reversed = True

        if reversed and arr[i] < arr[i - 1]:
            r = i

        if reversed and arr[i] > arr[i - 1]:
            break

        i += 1

    subArr = arr[l : r + 1]
    subArr.reverse()
    newArr = arr[0 : l] + subArr + arr[r + 1 :]
    j = 1
    while j < n:
        if newArr[j] < newArr[j - 1]:
            print('no')
            return
        j += 1

    print('yes')
    print(l + 1, r + 1)
    return

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution(n, arr)

# 'yes' only if exist 1 segment [l, r]
# otherwise, 'no'