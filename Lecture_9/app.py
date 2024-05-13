import queue

def BFS(s, f):
    q = queue.Queue()
    q.put(s)
    dist[s] = 0

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)

            if v == f:
                return

N = int(input().strip())
input()

for _ in range(N):
    dict = []

    while True:
        word = input()
        if word == "*": break
        dict.append(word)

    V = len(dict)
    graph = [[] for _ in range(V)]

    for u in range(V - 1):
        for v in range(u + 1, V):
            if len(dict[u]) == len(dict[v]):
                count = 0

                for i in range(len(dict[u])):
                    if dict[u][i] != dict [v][i]: count += 1

                if count == 1:
                    graph[u].append(v)
                    graph[v].append(u)

    while True:
        try:
            line = input()
            if line == '': break
        except EOFError: break

        sWord, fWord = line.split()
        s = dict.index(sWord)
        f = dict.index(fWord)
        dist = [-1] * V
        BFS(s, f)
        print(f"{sWord} {fWord} {dist[f]}")

    print()
