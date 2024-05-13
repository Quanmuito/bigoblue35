# https://codeforces.com/problemset/problem/242/B

def convert(str): return int(str)

def sortByFirstElement(arr): return arr[0]
def sortByLastElement(arr): return arr[1]

totalLines = convert(input())

nbrOfLines = 0
lines = list([])
while (nbrOfLines < totalLines):
    lines.append(list(map(convert, input().split(' '))))
    nbrOfLines += 1

originalLines = lines.copy()

lines.sort(key = sortByFirstElement)
lowestPoint = lines[0][0]

lines.sort(key = sortByLastElement)
highestPoint = lines[-1][1]

linesHasLowestPoint = list([])
for line in lines:
    if (line[0] == lowestPoint): linesHasLowestPoint.append(line)

linesHasBothPoint = list([])
for line in linesHasLowestPoint:
    if (line[1] == highestPoint): linesHasBothPoint.append(line)

if (len(linesHasBothPoint) > 0):
    for i in range(0, len(originalLines)):
        current = originalLines[i]
        if (current[0] == lowestPoint and current[1] == highestPoint): print(i + 1)
else: print(-1)