import queue

N = int(input().strip())

minHeap = queue.PriorityQueue()
maxHeap = queue.PriorityQueue()
total = 0
billId = 0
taken = [False] * 1000005

for _ in range(N):
    info = list(map(int, input().strip().split(' ')))

    for i in range(info[0]):
        billId += 1
        minHeap.put((info[i + 1], billId))
        maxHeap.put((-info[i + 1], billId))

    while taken[minHeap.queue[0][1]]:
        minHeap.get()
    minBill = minHeap.get()
    taken[minBill[1]] = True

    while taken[maxHeap.queue[0][1]]:
        minHeap.get()
    maxBill = maxHeap.get()
    taken[maxBill[1]] = True

    total += - maxBill[0] - minBill[0]

print(total)

# Optimize
import heapq

taken = [False] * 1000005
maxHeap = []
minHeap = []
money = 0
nbills = 0

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))

    for x in a[1:]:
        nbills += 1
        heapq.heappush(maxHeap, (-x, nbills))
        heapq.heappush(minHeap, (x, nbills))

    while taken[maxHeap[0][1]]:
        heapq.heappop(maxHeap)

    while taken[minHeap[0][1]]:
        heapq.heappop(minHeap)

    taken[maxHeap[0][1]] = taken[minHeap[0][1]] = True
    money += -heapq.heappop(maxHeap)[0] - heapq.heappop(minHeap)[0]

print(money)