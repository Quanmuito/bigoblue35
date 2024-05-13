# https://codeforces.com/problemset/problem/572/A

def convert(string): return int(string)

[lenA, lenB] = list(map(convert, input().split(' ')))
[k, m] = list(map(convert, input().split(' ')))

listA = list(map(convert, input().split(' ')))
listB = list(map(convert, input().split(' ')))

listA.sort()
listB.sort()

selectedA = listA[0 : k]
selectedB = listB[(lenB - m) : ]

# Highest of A is smaller than lowest of B
print('YES' if (selectedA[-1] < selectedB[0]) else 'NO')