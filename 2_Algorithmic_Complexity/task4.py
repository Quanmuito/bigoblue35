# https://codeforces.com/problemset/problem/161/A

def solution(n, m, x, y, arrA, arrB):
    pairs = []
    i = j = 0
    while i < n and j < m:
        need = arrA[i]
        size = arrB[j]

        if (need - x <= size and need + y >= size):
            pairs.append([i + 1, j + 1])
            i += 1
            j += 1
        else:
            if need < size: i += 1
            else: j += 1

    print(len(pairs))
    for a, b in pairs:
        print(a, b)


# Input
n, m, x, y = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# Output
solution(n, m, x, y, arrA, arrB)

# Start from the beginning,
# If find 2 indexes i and j satisfy, move to index (i + 1) and (j + 1)
# If not satisfy, move index of the one with smaller value + 1 (increase the smaller value)

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)