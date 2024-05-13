# https://codeforces.com/problemset/problem/892/B

def solution(n, arr):
    alive = 0
    i = left = n - 1

    while i >= 0:
        current = arr[i]

        if current != 0:
            reach = i - current
            if reach <= 0:
                alive += 1
                break
            if left > reach: left = reach
        else:
            if i == left:
                alive += 1
                left = i - 1

        i -= 1

    print(alive)
    return

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution(n, arr)

# 'left' is the index of the first person alive after a chain of claws

# Time Complexity: O(n)
# Space Complexity: O(n)