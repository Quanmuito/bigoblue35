import heapq
import math

N = int(input().strip())

reviews = []
box = []
for _ in range(N):
    info = list(map(int, input().strip().split(' ')))

    if info[0] == 1: heapq.heappush(reviews, -info[1])
    else:
        num = math.floor(len(reviews) / 3)
        if num == 0: print('No reviews yet')
        else:
            for _ in range(num):
                box.append(heapq.heappop(reviews))
            print(-box[-1])

            while len(box) > 0: heapq.heappush(reviews, box.pop())

# Optimize

import heapq
top3 = []
rest = []
nreviews = 0

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    type = line[0]

    if type == 1:
        x = line[1]
        nreviews += 1

        if len(top3) != 0 and top3[0] < x:
            heapq.heappush(rest, -heapq.heappop(top3))
            heapq.heappush(top3, x)
        else:
            heapq.heappush(rest, -x)

        if nreviews % 3 == 0:
            heapq.heappush(top3, -heapq.heappop(rest))
    else:
        if len(top3) == 0:
            print("No reviews yet")
        else:
            print(top3[0])