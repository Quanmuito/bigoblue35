import queue

N = int(input())
A = list(map(int, input().split()))
heap = queue.PriorityQueue()

for i in range(N):
	heap.put(-A[i])

	if i < 2:
		print(-1)
	else:
		first = -heap.get()
		second = -heap.get()
		third = -heap.get()

		print(first * second * third)

		heap.put(-first)
		heap.put(-second)
		heap.put(-third)