# def solution(n, arr):
#     maxLength = 0
#     minPoint = arr[0]
#     minPointIndex = 0
#     maxPoint = arr[0]
#     maxPointIndex = 0
#     startIndex = 0

#     i = 0
#     while i < n:
#         current = arr[i]

#         if minPoint >= current:
#             minPoint = current
#             minPointIndex = i
#         elif maxPoint <= current:
#             maxPoint = current
#             maxPointIndex = i

#         if maxPoint - minPoint > 1:
#             maxLength = max(maxLength, i - startIndex)

#             i = min(minPointIndex, maxPointIndex)
#             minPoint = maxPoint = arr[i + 1]
#             startIndex = i + 1

#         i +=

#     print(max(maxLength, i - startIndex))
#     return

# # Input
# n = int(input())
# arr = list(map(int, input().split()))

# # Output
# solution(n, arr)

def solution2(n, arr):
    right = 0
    best = 0
    count = 0
    fre = {}

    for left in range(n):
        while right < n:
            if arr[right] not in fre:
                if count == 2: break
                count += 1
            fre[arr[right]] += 1
            right += 1

        best = max(best, right - left + 1)

        if fre[arr[left] == 1]:
            count -= 1
        fre[arr[left]] -= 1

    print(best)


# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
solution2(n, arr)

