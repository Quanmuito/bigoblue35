# https://acm.timus.ru/problem.aspx?space=1&num=1585
# Complexity: O(N)

n = int(input())
A = dict()

for _ in range(n):
    name = input()
    if name in A: A[name] += 1
    else: A[name] = 1

output = ''
maxNum = 0
for name, number in A.items():
    if maxNum < number:
        output = name
        maxNum = number

print(output)