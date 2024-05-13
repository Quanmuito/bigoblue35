# https://codeforces.com/problemset/problem/673/A

def convert(string): return int(string)

nbrOfPeaks = int(input())
peaks = list(map(convert, input().split(' ')))

def getTime():
    last = 0

    for peak in peaks:
        boring = peak - last

        if (boring > 15): return last + 15
        else: last = peak

    output = last + 15
    return output if (output < 90) else 90

print(getTime())