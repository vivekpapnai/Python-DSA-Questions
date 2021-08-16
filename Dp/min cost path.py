import sys
from sys import stdin

MAX_VALUE = 2147483647


def minCostPath(mat, mRows, nCols, m, n, dp):
    if m == mRows - 1 and n == nCols - 1:
        return mat[m][n]
    if m >= mRows or n >= nCols:
        return sys.maxsize
    # minimumCost = sys.maxsize
    if dp[m + 1][n] == sys.maxsize:
        ans1 = minCostPath(mat, mRows, nCols, m + 1, n, dp)
        dp[m + 1][n] = ans1
    else:
        ans1 = dp[m + 1][n]
    if dp[m][n + 1] == sys.maxsize:
        ans2 = minCostPath(mat, mRows, nCols, m, n + 1, dp)
        dp[m][n + 1] = ans2
    else:
        ans2 = dp[m][n + 1]
    if dp[m + 1][n + 1] == sys.maxsize:
        ans3 = minCostPath(mat, mRows, nCols, m + 1, n + 1, dp)
        dp[m + 1][n + 1] = ans3
    else:
        ans3 = dp[m + 1][n + 1]
    minimumCost = mat[m][n] + min(ans1, ans2, ans3)

    return minimumCost


# Your code goes here

def minCostPathIter(mat, mRows, nRows, m, n):
    dp = [[sys.maxsize for j in range(nCols + 1)] for i in range(mRows + 1)]
    for i in range(mRows - 1, -1, -1):
        for j in range(nCols - 1, -1, -1):
            if i == mRows - 1 and j == nRows - 1:
                dp[i][j] = mat[i][j]
            else:
                ans1 = dp[i + 1][j]
                ans2 = dp[i][j + 1]
                ans3 = dp[i + 1][j + 1]
                dp[i][j] = mat[i][j] + min(ans1, ans2, ans3)

    return dp[0][0]


# taking input using fast I/O method
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])

    if mRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


# main
mat, mRows, nCols = take2DInput()
# dp = [[sys.maxsize for j in range(nCols + 1)] for i in range(mRows + 1)]
print(minCostPathIter(mat, mRows, nCols, 0, 0))
