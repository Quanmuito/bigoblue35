# https://www.spoj.com/problems/EKO/
# Complexity: O(N * a[0]). a[0] is the height of the highest tree

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

minH = 0 # minimum value of H
maxH = a[0] - 1 # maximum value of H
res = 0

while minH <= maxH:
    H = (minH + maxH) // 2 # take the middle value to start

    total = 0
    for tree in a: # Check that this H satisfy or not
        if tree <= H: break
        total += tree - H

    if total >= M: # If the total of harvested wood still higher than M, increase minH to reduce harvested
        minH = H + 1
        res = H
        if total == M: # If satisfy, return the H
            break
    else: # Work the same but reverse
        maxH = H - 1

print(res)