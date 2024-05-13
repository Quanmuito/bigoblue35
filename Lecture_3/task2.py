def solution(n, a, b, arr: list):
    arr.sort()
    output = 0

    maxVasya = arr[b - 1]
    minPetya = arr[b]

    while maxVasya < minPetya:
        output += 1
        minPetya -= 1

    print(output)
    return

# Input
n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

# Output
solution(n, a, b, arr)