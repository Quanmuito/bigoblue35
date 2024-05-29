# https://codeforces.com/problemset/problem/518/B?locale=en
# Complexity: O(S + T)

s = input()
distS = dict()
for char in s:
    if char in distS:
        distS[char] += 1
    else:
        distS[char] = 1

t = input()
distT = dict()
for char in t:
    if char in distT:
        distT[char] += 1
    else:
        distT[char] = 1

yay = 0
for char, count in distT.items():
    if char in distS:
        if count > distS[char]:
            yay += distS[char]
            distT[char] -= distS[char]
            distS[char] = 0
        else:
            yay += count
            distS[char] -= count
            distT[char] = 0

whoop = 0
for char, count in distS.items():
    if count == 0: continue

    if char.isupper():
        char = char.lower()
    else:
        char = char.upper()

    if char in distT and distT[char] > 0:
        if distT[char] > count:
            whoop += count
        else:
            whoop += distT[char]

print(yay, whoop)