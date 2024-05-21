# Complexity: O(log N)

def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return mid

        if a[mid] > x:
            return binarySearch(a, left, mid - 1, x)

        return binarySearch(a, mid + 1, right, x)

    return -1

def binarySearchFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if (mid == left or x != a[mid - 1]) and a[mid] == x:
            return mid

        if a[mid] > x:
            return binarySearchFirst(a, mid + 1, right, x)

        return binarySearchFirst(a, left, mid - 1, x)

    return -1

def binarySearchLast(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2

        if (mid == right or x != a[mid + 1]) and a[mid] == x:
            return mid

        if a[mid] > x:
            return binarySearchLast(a, mid + 1, right, x)

        else:
            return binarySearchLast(a, left, mid - 1, x)

    return -1

n, x = map(int, input().split())
a = list(map(int, input().split()))
res = binarySearch(a, 0, n - 1, x)