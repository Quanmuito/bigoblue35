# https://vjudge.net/problem/UVA-10226
# Complexity: O(N log N)

import sys

T = int(input())
try:
    input()
    for tc in range(T):
        dist = dict()
        count = 0

        while True:
            line = input()
            if line == '': break
            count += 1
            if line in dist:
                dist[line] += 1
            else:
                dist[line] = 1

        for name, number in sorted(dist.items()):
            print('{} {:.4f}'.format(name, number * 100 / count))

        if tc < T - 1:
            print()
except EOFError:
    for name, number in sorted(dist.items()):
        print('{} {:.4f}'.format(name, number * 100 / count))
    sys.exit(0)