from sys import stdin


def LIS(arr, i, n, dp):
    if i == n:
        return 0, 0
    includingSize = 1
    for j in range(i + 1, n):
        if arr[j] >= arr[i]:
            if dp[j] == -1:
                ans = LIS(arr, j, n, dp)
                dp[j] = ans
                further_including_Size = ans[0]
            else:
                further_including_Size = dp[j][0]
            includingSize = max(includingSize, 1 + further_including_Size)

    if dp[i + 1] == -1:
        ans = LIS(arr, i + 1, n, dp)
        dp[i+1] = ans
        excludingSize = ans[1]
    else:
        excludingSize = dp[i + 1][1]
    maxSize = max(includingSize, excludingSize)
    return includingSize, maxSize

def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
dp = [-1 for x in range(n + 1)]
print(LIS(arr, 0, n, dp)[1])
