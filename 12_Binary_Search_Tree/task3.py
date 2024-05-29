# https://codeforces.com/problemset/problem/424/B
# Complexity: O(N) with N is number of locations

n, s = map(int, input().split())

locations = []
for _ in range(n):
    x, y, k = map(int, input().split())
    distance = (x ** 2 + y ** 2) ** 0.5
    locations.append((distance, k))

locations = sorted(locations)
minR = 0
for distance, population in locations:
    s += population
    minR = distance
    if s >= 1000000: break

if s < 1000000: print(-1)
else: print('{:.7f}'.format(minR))