# https://codeforces.com/problemset/problem/518/A

input1 = input()
input2 = input()

sequence = 'abcdefghijklmnopqrstuvwxyz'

def lastCharUp(str):
    lastCharIndex = sequence.index(str[-1])
    indexUp = (len(sequence) + lastCharIndex + 1) % len(sequence)
    return str[:-1] + sequence[indexUp]

def getString():
    if (input1 == input2): return 'No such string'

    breakpoint = 0
    for i in range(0, len(input1)):
        index1 = sequence.index(input1[i])
        index2 = sequence.index(input2[i])

        if (index1 < index2):
            breakpoint = i
            break

    # Breakpoint at last character => last char go up
    if (breakpoint == len(input1) - 1): output = lastCharUp(input1)
    else:
        nextBreakpoint = breakpoint + 1
        nextBreakpointIndex = sequence.index(input1[nextBreakpoint])

        # If the character next to breakpoint is 'z' => breakpoint to last char go up
        if (nextBreakpointIndex == 25):
            breakpointIndexUp = sequence.index(input1[breakpoint]) + 1
            output = input1[0 : breakpoint] + sequence[breakpointIndexUp]

            restOfInput1 = input1[nextBreakpoint : ]
            for char in restOfInput1:
                index = sequence.index(char)
                indexUp = (len(sequence) + index + 1) % len(sequence)
                output += sequence[indexUp]
        else:
            output = lastCharUp(input1)

    return output if ((output > input1) & (output < input2)) else 'No such string'

print(getString())
