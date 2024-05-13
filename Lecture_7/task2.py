import heapq

Q = int(input())
heap = []
change = False

for _ in range(Q):
    _input = input().strip()

    if len(_input) == 1:
        if change:
            heapq.heapify(heap)
            change = False
        print(heap[0])
    else:
        mode, value = map(int, _input.split(' '))
        if mode == 1: heap.append(value)
        if mode == 2: heap.remove(value)
        change = True

# Optimize

import queue

q = int(input())
pq = queue.PriorityQueue()
pqRemove = queue.PriorityQueue()

for i in range(q):
    line = input()

    if line[0] == '1':
        value = int(line.split()[1])
        pq.put(value)
    elif line[0] == '2':
        value = int(line.split()[1])
        pqRemove.put(value)
    else:
        while not pqRemove.empty() and pq.queue[0] == pqRemove.queue[0]:
            pq.get()
            pqRemove.get()

        print(pq.queue[0])