# https://codeforces.com/problemset/problem/602/B

def solution2(n, arr):
    right = 0
    best = 0
    count = 0
    fre = {}

    for left in range(n):
        while right < n:
            if arr[right] not in fre:
                if count == 2: break
                count += 1
            fre[arr[right]] += 1
            right += 1

        best = max(best, right - left + 1)

        if fre[arr[left] == 1]:
            count -= 1
        fre[arr[left]] -= 1

    print(best)


# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution2(n, arr)

