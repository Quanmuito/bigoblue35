# https://vjudge.net/problem/UVA-10341

import math

def equation(x: float):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x ** 2 + u

while True:
    try:
        p, q, r, s, t, u = map(float, input().split())

        if equation(1.0) > 1e-9 or p + r + u < 0:
            print("No solution")
            continue

        minX = 0
        maxX = 1

        for i in range(100):
            mid = (minX + maxX) / 2

            value = equation(mid)

            if value > 0:
                minX = mid
            else:
                maxX = mid

        print('{:0.4f}'.format(minX))
    except EOFError:
        break