mass = {'C': 12, 'H': 1, 'O': 16}
number = ['2', '3', '4', '5', '6', '7', '8', '9']
precedence = {'+': 1, '*': 2}

def getRPN(expression: str):
    opStack = []
    output = []

    for char in expression:
        if char in mass: output.append(int(mass[char]))
        elif char in number: output.append(int(char))
        # if char in mass: output.append(char)
        # elif char in number: output.append(char)
        elif char == '(': opStack.append(char)
        elif char == ')':
            while len(opStack) > 0 and opStack[-1] != '(': output.append(opStack.pop())
            opStack.pop()
        else:
            while len(opStack) > 0 and precedence.get(opStack[-1], 0) >= precedence[char]: output.append(opStack.pop())
            opStack.append(char)
    while len(opStack) > 0: output.append(opStack.pop())

    return output

def evaluateRPN(rpn: list):
    stack = []

    while len(rpn) > 0:
        token = rpn.pop(0)

        if isinstance(token, int): stack.append(token)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if token == '+': stack.append(op1 + op2)
            elif token == '*': stack.append(op1 * op2)
    return stack.pop()

def solve(string: str):
    if '(' in string and ')' in string:
        openBracketIndex = []
        i = 0
        while i < len(string):
            current = string[i]

            if current == '(': openBracketIndex.append(i)
            elif current == ')':
                if i < len(string) - 1 and string[i + 1] in number:
                    openBracketIndex.pop()
                else:
                    l = openBracketIndex.pop()
                    string = string[0 : l] + string[l + 1 : i] + string[i + 1 : ]
                    i -= 2
            i += 1

    expression = ''
    for char in string:
        if char in mass or char == '(':
            if len(expression) == 0 or expression[-1] == '(':
                expression += char
            else:
                expression += '+' + char
        elif char in number:
            expression += '*' + char
        else: expression += char

    rpn = getRPN(expression)
    return evaluateRPN(rpn)


# Input
string = input()

# Output
print(solve(string))