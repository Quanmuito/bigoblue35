import queue

while True:
    N = int(input().strip())
    if N == 0: break

    q = queue.PriorityQueue(5000)
    A = list(map(int, input().strip().split(' ')))

    for num in A: q.put(num)

    cost = 0
    while q.qsize() > 1:
        n1 = q.get()
        n2 = q.get()
        cost += n1 + n2
        q.put(n1 + n2)

    print(cost)