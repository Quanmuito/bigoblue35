# https://vjudge.net/problem/UVA-10611
# Complexity: O(Q * log N)

def searchShorter(a, left, right, x):
    if a[-1] < x: return N - 1

    if left <= right:
        mid = (left + right) // 2

        if a[mid] < x and a[mid + 1] >= x:
            return mid

        if a[mid] >= x:
            return searchShorter(a, left, mid - 1, x)

        return searchShorter(a, mid + 1, right, x)

    return -1

def searchHigher(a, left, right, x):
    if a[0] > x: return 0

    if left <= right:
        mid = (left + right) // 2

        if a[mid] > x and a[mid - 1] <= x:
            return mid

        if a[mid] > x:
            return searchHigher(a, left, mid - 1, x)

        return searchHigher(a, mid + 1, right, x)

    return -1

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
H = list(map(int, input().split()))

for h in H:
    shorter = searchShorter(A, 0, N - 1, h)
    higher = searchHigher(A, 0, N - 1, h)
    print('{} {}'.format(A[shorter] if shorter != -1 else 'X', A[higher] if higher != -1 else 'X'))