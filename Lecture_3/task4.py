def solution(n: int, arr: list):
    unique = list(set(arr))
    unique.sort()
    unique.reverse()
    count = {}

    for x in unique:
        count[x] = arr.count(x)

    place = {}
    place[unique[0]] = 1

    i = 1
    while i < len(unique):
        place[unique[i]] = place[unique[i - 1]] + count[unique[i - 1]]
        i += 1

    output = ''
    for x in arr:
        output += f"{place[x]} "

    print(output)

    return

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution(n, arr)