# https://codeforces.com/problemset/problem/731/A

input = input()
sequence = 'abcdefghijklmnopqrstuvwxyz'

output = 0
lastIndex = 0
totalDistance = len(sequence)

for char in input:
    currentIndex = sequence.index(char)
    distance1 = abs(currentIndex - lastIndex)
    distance2 = totalDistance - distance1

    output += distance1 if (distance1 < distance2) else distance2

    lastIndex = currentIndex

print(output)