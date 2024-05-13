# https://codeforces.com/problemset/problem/279/B

def solution(n, t, arr):
    max = 0
    nbrOfBooks = 0
    totalTime = 0
    iStart = 0

    i = 0
    while i < n:
        totalTime += arr[i]

        if totalTime == t:
            nbrOfBooks = i - iStart + 1

        if totalTime > t:
            nbrOfBooks = i - iStart
            totalTime -= arr[iStart] + arr[i]
            i -= 1
            iStart += 1

        if nbrOfBooks > max: max = nbrOfBooks
        i += 1

    if (totalTime <= t):
        nbrOfBooks = i - iStart
        if nbrOfBooks > max: max = nbrOfBooks

    return max
# Input
n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(solution(n, t, arr))

# Concept: Start with index i, find an index j that sum of arr[i, j] >= t
# Next, find an index k that sum of arr[i + 1, k] >= t
# Repeat
# Find the array that has maximum length

# Time Complexity: O(n)
# Space Complexity: O(1)