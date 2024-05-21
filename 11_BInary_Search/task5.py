# https://vjudge.net/problem/UVA-12032
# Complexity: O(T * n * a[-1])

T = int(input())
for tc in range(T):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    minK = 1 # The minimum value of k
    maxK = a[-1] + 1 # The maximum of k to jumb from 0 to highest step
    res = 0

    while minK <= maxK:
        mid = (minK + maxK) // 2 # take the middle value
        k = mid
        check = True

        for i in range(n + 1): # try to climb with the current k
            if a[i] - a[i - 1] > k:
                check = False
                break
            elif a[i] - a[i - 1] == k:
                k -= 1

        if check: # if the current value is able to climb, update res, start decrease from this point to check if there is any lower value still satisfy
            res = mid
            maxK = mid - 1
        else: # Work the same but reverse
            minK = mid + 1

        # In case of decreasing maxK till reach the needed value k -> update the output -> Decrease the bound 1 more time will make 'check=False' -> minK = mid + 1, maxK = mid - 1 -> end loop
        # In case of increasing minK till reach the needed value k -> check=True -> update output -> run the step above

    print('Case {}: {}'.format(tc + 1, res))