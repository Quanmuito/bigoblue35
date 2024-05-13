def solution(n, k, arr):
    distinct = {}
    count = 0

    for i in range(n):
        current = arr[i]
        if current not in distinct:
            count += 1

        distinct[current] = i

        if count == k:
            sortedDistinct = sorted(distinct.items(), key = lambda x:x[1])
            for _, value in sortedDistinct:
                return f"{value + 1} {i + 1}"


    return '-1 -1'

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(solution(n, k, arr))

# Loop through the array, increase the counter if new distinct element appear and save the last index of that element to a dictionary.
# When the counter reachs 'k', the current index will be the 'right end'.
# Sort the dictionary by value (index), the lowest index will be the 'left end'
# If the counter never reach 'k' => not enough distinct characters.

# Time Complexity: O(n)
# Space Complexity: min: O(n + k)

def optimalSolution(n, k, arr):
    distinct = {}
    count = 0

    for i in range(n):
        current = arr[i]
        if current not in distinct:
            count += 1

        distinct[current] += 1

        if count == k:
            j = 0
            while True:
                if distinct[arr[j]] > 1: distinct[arr[j]] -= 1
                else: return f"{j + 1} {i + 1}"
                j += 1


    return '-1 -1'

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(optimalSolution(n, k, arr))