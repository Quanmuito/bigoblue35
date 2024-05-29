# https://vjudge.net/problem/URAL-1837
# Complexity:
# - Make graph: O(N * L) with N is number of lines and L is the number of names in 1 line
# - Make dist and visited: O(M) with M is the number of unique names
# - BFS: O(M + C) with C is number of connections in graph[each unique name]
# - Check 'Isenbaev' in names: O(M)
# - Sort list and output: O(M log M)
# - Overall: O(N * L + M + C + M log M)

def BFS():
    q = ['Isenbaev']
    dist['Isenbaev'] = 0
    left = 0
    visited['Isenbaev'] = True

    while left < len(q):
        u = q[left]
        left += 1

        for v in graph[u]:
            if not visited[v] and v != u:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.append(v)

N = int(input())

names = set([])
graph = dict()
for _ in range(N):
    data = input().split()
    names.update(data)

    for name in data:
        if name in graph: graph[name].update(data)
        else: graph[name] = set(data)

dist = dict()
visited = dict()
for name in names:
    dist[name] = -1
    visited[name] = False

if 'Isenbaev' in names: BFS()

for name in sorted(list(names)):
    print('{} {}'.format(name, dist[name] if dist[name] != -1 else 'undefined'))