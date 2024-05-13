def solution(m, n, arrA, arrB):
    i = 0
    j = 0
    count = m
    while i < len(arrA) and j < len(arrB):
        if arrA[i] > arrB[j]:
            j += 1
        elif arrA[i] <= arrB[j]:
            i += 1
            j += 1
            count -= 1
    return count

# Input
m, n = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# Output
print(solution(m, n, arrA, arrB))

# Assume George have to come up with all problems with required complexity.
# Loop through both array at the same time with 2 separated index i and j.
# If required complexity larger than prepared -> compare to the next element from prepared list
# If required complexity equal or smaller than prepared -> move both to the next element and reduce number of problems need to come up

# Time Complexity: O(m + n)
# Space Complexity: O(m + n)