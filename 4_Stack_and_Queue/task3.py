def solve(n: int):
    arr = [i + 1 for i in range(n)]

    discard = []
    while len(arr) > 1:
        discard.append(arr.pop(0))
        arr.append(arr.pop(0))

    if len(discard) == 0: print('Discarded cards:')
    else: print('Discarded cards:', ', '.join(list(map(str, discard))))
    print('Remaining card:', arr[0])
    return

# Input
cases = []
while True:
    value = int(input())
    if (value == 0):
        break
    cases.append(value)

# Output
for x in cases:
    solve(x)
