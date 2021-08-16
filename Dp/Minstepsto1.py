# You have to move a number n from n to 1 in the minimum possible steps and the allowed operations are:
# 1. you can do n-1
# 2. you can do n/2 only if n is divisible by 2
# 3. you can do n/2 only if nn is divisible by 3
import sys


def minSteps1(n, dp):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    ans2 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans1 = minSteps1(n // 3, dp)
            dp[n // 3] = ans1
        else:
            ans1 = dp[n // 3]
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minSteps1(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]
    if dp[n - 1] == -1:
        ans3 = minSteps1(n - 1, dp)
        dp[n - 1] = ans3
    else:
        ans3 = dp[n - 1]

    return 1 + min(ans1, ans2, ans3)


def minStepsTo1DP(n):
    storage = [-1] * (n + 1)
    storage[0] = 0
    storage[1] = 0
    bigNumber = 2147483647
    for i in range(2, n + 1):
        op1 = storage[i - 1]
        op2 = storage[i // 2] if i % 2 == 0 else bigNumber
        op3 = storage[i // 3] if i % 3 == 0 else bigNumber
        storage[i] = 1 + min(op1, op2, op3)
    return storage[n]


n = int(input())
print(minStepsTo1DP(n))

#
# n = int(input())
# dp = [-1 for i in range(n + 1)]
# print(minSteps1(n, dp))
