operators = ['+', '-', '*', '/', '^']

def solve(t: int, arr: list):
    for expression in arr:
        output = ''
        opStack = []
        for char in expression:
            if char in operators: opStack.append(char)
            elif char == '(': continue
            elif char == ')': output += opStack.pop()
            else: output += char
    print(output)

    return

# Input
t = int(input())

i = 0
arr = []
while i < t:
    arr.append(input())
    i += 1

# Output
solve(t, arr)