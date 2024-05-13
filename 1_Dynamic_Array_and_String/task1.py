# https://codeforces.com/problemset/problem/691/A

nbrOfPins = int(input())
sequence = input().split(' ')

open = sequence.count('0')
correct = (nbrOfPins == 1 and open == 0) or (nbrOfPins > 1 and open == 1)
print('YES' if correct else 'NO')