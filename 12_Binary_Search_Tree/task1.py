# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/
# Complexity: O(T * N * log N) with T is number of test cases, N is the number of elements

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = set(map(int, input().split()))

    res = len(A)
    if res == X: print('Good')
    else: print('Bad' if res < X else 'Average')