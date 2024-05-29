# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/
# Complexity:
# - Create set: O(N)
# - Check element in set: O(1), worst: O(N)
# - Add element to set: O(1), worst: O(N)
# - Overall: O(M + N), worst: O(N + N * M)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    exist = set(A[0 : N])
    for i in range(M):
        print('YES' if A[i + N] in exist else 'NO')
        exist.add(A[i + N])