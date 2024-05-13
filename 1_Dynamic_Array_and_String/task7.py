# https://codeforces.com/problemset/problem/721/B

import math
def convert(string): return int(string)

[n, k] = list(map(convert, input().split(' ')))

nbrOfPasswords = 0
passwords = list([])

while (nbrOfPasswords < n):
    passwords.append(input())
    nbrOfPasswords += 1

correctPassword = input()

def sortByLength(string): return len(string)
passwords.sort(key = sortByLength)

lessChar = 0
equalChar = 0

for password in passwords:
    if (len(password) < len(correctPassword)): lessChar += 1
    if (len(password) == len(correctPassword)): equalChar += 1

# Best case
bestCase = lessChar + 1
bestTimeoutTime = math.ceil(bestCase / k) - 1
bestCaseTime = bestTimeoutTime * 5 + bestCase * 1

worstCase = lessChar + equalChar
worstTimeoutTime = math.ceil(worstCase / k) - 1
worstCaseTime = worstTimeoutTime * 5 + worstCase * 1

print(bestCaseTime, worstCaseTime)