import queue
s = []
q = queue.Queue()
pq = queue.PriorityQueue()

while True:
    try:
        n = int(input())
    except EOFError:
        break

    s.clear()
    q.queue.clear()
    pq.queue.clear()
    isStack = isQueue = isPQ = True

    for _ in range(n):
        type, x = map(int, input().split())
        if type == 1:
            s.append(x)
            q.put(x)
            pq.put(-x)
        else:
            if len(s) == 0:
                isStack = isQueue = isPQ = False
            else:
                if x != s.pop():
                    isStack = False
                if x != q.get():
                    isQueue = False
                if x != -pq.get():
                    isPQ = False

    if isStack + isQueue + isPQ == 0:
        print("impossible")
    elif isStack + isQueue + isPQ > 1:
        print("not sure")
    elif isStack:
        print("stack")
    elif isQueue:
        print("queue")
    else:
        print("priority queue")