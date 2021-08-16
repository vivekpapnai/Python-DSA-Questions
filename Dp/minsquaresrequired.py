import math
import sys


def minSquare(n, dp):
    if n == 0:
        return 0
    i = 1
    maintains = sys.maxsize
    while i * i <= n:
        x = n - (i ** 2)
        if dp[x] == -1:
            ans1 = minSquare(x, dp)
            dp[x] = ans1
            ans = ans1 + 1
        else:
            ans = 1 + dp[x]
        maintains = min(maintains, ans)
        i += 1
    return maintains


def minSquareMemo(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        minAns = 2147483647
        while j**2 <= i:
            ans = dp[i - (j * j)]
            minAns = min(minAns, ans)
            j += 1
        dp[i] = minAns + 1

    return dp[n]


n = int(input())
# dp = [-1] * (n + 1)
# dp[0] = 0
print(minSquareMemo(n))
