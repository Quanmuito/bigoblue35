N = int(input().strip())

topics = []
for _ in range(N):
    ID, Z, P, L, C, S = map(int, input().strip().split(' '))
    newZ = P * 50 + L * 5 + C * 10 + S * 20
    topics.append((newZ - Z, ID, newZ))
topics.sort(reverse = True)

for i in range(5):
    topic = topics[i]
    print(topic[1], topic[2])