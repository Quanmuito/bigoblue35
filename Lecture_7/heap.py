def minHeapify(i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    if right < len(h) and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        minHeapify(smallest)

def buildMinHeap(n):
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(i)

h = [7, 12, 6, 10, 17, 15, 2, 4]
buildMinHeap(len(h))
print(h)

def maxHeapify(i):
    highest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(h) and h[left] > h[highest]:
        highest = left
    if right < len(h) and h[right] > h[highest]:
        highest = right
    if highest != i:
        h[i], h[highest] = h[highest], h[i]
        maxHeapify(highest)

def buildMaxHeap(n):
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(i)

h = [7, 12, 6, 10, 17, 15, 2, 4]
buildMaxHeap(len(h))
print(h)

def push(value):
    h.append(value)
    i = len(h) - 1
    while i != 0 and h[(i - 1) // 2] < h[i]:
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2