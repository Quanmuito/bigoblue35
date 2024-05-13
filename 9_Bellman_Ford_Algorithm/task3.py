K, N, W = list(map(int, input().strip().split(' ')))

price = 0
for i in range(W):
    price += (i + 1) * K

print(price - N if price > N else 0)