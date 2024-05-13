from queue import Queue

def solve(main, lock, keys: list):
    dist = [-1] * 100000
    q = Queue()
    q.put(main)
    dist[main] = 0

    while not q.empty():
        u = q.get()

        for key in keys:
            v = (key * u) % 100000

            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)

                if v == lock: return dist[v]

    return -1

main, lock = list(map(int, input().split(' ')))
n = int(input())
keys = list(map(int, input().split(' ')))
keys.sort()

print(solve(main, lock, keys))