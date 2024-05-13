# https://codeforces.com/problemset/problem/448/B

def hasCommonChars(str1, str2):
    hasCommonChars = True

    for char in str1:
        # Find the character in str2
        charIndex = str2.find(char)
        # If character exist, remove it from str2
        if (charIndex != -1): str2 = str2.replace(char, '', 1)
        # If any character is not exist, they don't have common characters
        else:
            hasCommonChars = False
            break

    return hasCommonChars

# Assume that 2 strings have common character, check those character order
def hasCommonCharsInOrder(str1, str2):
    commonOrder = True
    lastIndex = 0

    for char in str1:
        # Go through each character in str1
        # If found in str2, find the next character from that character in str2 to the end
        lastIndex = str2.find(char, lastIndex)

        if (lastIndex == -1):
            commonOrder = False
            break

    return commonOrder

def getMethod(str1, str2):
    if (len(str1) == len(str2)):
        return 'array' if (hasCommonChars(str1, str2)) else 'need tree'

    if str1 in str2:
        return 'automaton'
    else:
        if (hasCommonChars(str1, str2)):
            return 'automaton' if (hasCommonCharsInOrder(str1, str2)) else 'both'
        else: return 'need tree'

input1 = input()
input2 = input()

print(getMethod(input2, input1))