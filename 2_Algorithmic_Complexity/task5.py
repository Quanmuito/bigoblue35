# https://codeforces.com/problemset/problem/381/A

def isEven(num): return num % 2 == 0

def solution(n: int, arr: list):
    turn = scoreA = scoreB = 0

    while len(arr) > 0:
        first = arr[0]
        last = arr[-1]
        plus = 0
        if (first > last):
            plus = first
            arr.pop(0)
        else:
            plus = last
            arr.pop()

        if isEven(turn):
            scoreA += plus
        else:
            scoreB += plus

        turn += 1

    print(scoreA, scoreB)
    return


# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution(n, arr)

# Time Complexity: O(n)
# Space Complexity: O(1)