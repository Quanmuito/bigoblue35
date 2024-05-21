# https://www.spoj.com/problems/OPCPIZZA/
# Complexity: O(n^2)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == m: count += 1

    print(count)

# Optimize: O(n * log n)

T = int(input())

def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return mid

        if a[mid] > x:
            return binarySearch(a, left, mid - 1, x)

        return binarySearch(a, mid + 1, right, x)

    return -1

for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    count = 0
    for i in range(n):
        x = m - a[i]
        if (binarySearch(a, 0, n - 1, x) != -1): count += 1

    print(int(count / 2))