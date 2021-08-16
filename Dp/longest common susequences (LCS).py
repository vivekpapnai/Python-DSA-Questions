def LCS(str1, str2, i, j, dp):
    if i == len(str1) or j == len(str2):
        return 0
    if str1[i] == str2[j]:
        if dp[i][j] == -1:
            ans = 1 + LCS(str1, str2, i + 1, j + 1, dp)
            dp[i][j] = ans
        else:
            ans = dp[i][j]
    else:
        if dp[i][j + 1] == -1:
            ans1 = LCS(str1, str2, i, j + 1, dp)
            dp[i][j + 1] = ans1
        else:
            ans1 = dp[i][j + 1]
        if dp[i + 1][j] == -1:
            ans2 = LCS(str1, str2, i + 1, j, dp)
            dp[i + 1][j] = ans2
        else:
            ans2 = dp[i + 1][j]
        ans = max(ans1, ans2)

    return ans


def lcsIter(str1, str2):
    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    m = len(str1)
    n = len(str2)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


str1 = input()
str2 = input()
dp = [[-1 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
ans = lcsIter(str1, str2)
print(ans)
