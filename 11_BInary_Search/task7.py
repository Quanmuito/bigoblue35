# https://www.spoj.com/problems/HACKRNDM/
# Complexity: O(n^2)

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[j] > a[i] + k: break
        if a[j] - a[i] == k: count += 1

print(count)

# Optimize: O(n log n)

def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return mid

        if a[mid] > x:
            return binarySearch(a, left, mid - 1, x)

        return binarySearch(a, mid + 1, right, x)

    return -1

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

count = 0
for i in range(n):
    element = binarySearch(a, i, n - 1, a[i] + k)
    if element != -1: count += 1

print(count)