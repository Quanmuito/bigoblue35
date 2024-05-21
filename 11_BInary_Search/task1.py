# https://vjudge.net/problem/UVA-10474

MAX = 10005

def binarySearchFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if (mid == left or x != a[mid - 1]) and a[mid] == x:
            return mid

        if a[mid] < x:
            return binarySearchFirst(a, mid + 1, right, x)

        return binarySearchFirst(a, left, mid - 1, x)

    return -1

tc = 1
while True:
    N, Q = map(int, input().split())
    if N == 0 and Q == 0: break

    a = []

    for _ in range(N):
        a.append(int(input()))

    a.sort()
    print('CASE# {}:'.format(tc))
    tc += 1

    for _ in range(Q):
        x = int(input())
        res = binarySearchFirst(a, 0, N - 1, x)

        print('{} not found'.format(x)) if res == -1 else print('{} found at {}'.format(x, res + 1))