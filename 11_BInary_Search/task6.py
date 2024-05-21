# https://codeforces.com/problemset/problem/68/B
# Complexity: O(n * log a[-1])

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

total = sum(a)
k = k / 100

left = 0
right = a[-1]
while right - left > 1e-7:
    mid = (left + right) / 2
    transfer = 0
    for x in a:
        if x > mid: transfer += x - mid
    if mid * n < total - transfer * k:
        left = mid
    else:
        right = mid

print('%.9f' % left)