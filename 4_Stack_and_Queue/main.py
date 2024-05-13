def solve(string: str):
    if string[0] == '>': return 0
    ans = 0

    count = 0
    for i in range (len(string)):
        if string[i] == '<': count += 1
        else:
            if count == 0: break
            else:
                count -= 1
                ans = i + 1 if count == 0 else ans

    return ans

t = int(input())

for i in range(t):
    print(solve(input()))