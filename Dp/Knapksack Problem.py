def knapsack(n, w, wt, val, i,dp):
    if i == n:
        return
    if dp[i] == -1:
        ans1 = knapsack(n, w, wt, val, i + 1,dp)
        dp[i] = ans1
    else:
        ans1 = dp[i]
    if wt[i] <= w:
        if dp[i] == -1:
            ans2 = val[i] + knapsack(n, w - wt[i], wt, val, i + 1,dp)
            dp[i] = ans2
        else:
            ans2 = dp[i]
    else:
        ans2 = 0
        dp[i] = ans2

    ans = max(ans1, ans2)
    return ans


# def knapsack(n, w, wt, val, i,dp):
#     if i == n:
#         return 0
#     if wt[i] > w:
#         if dp[i] == -1:
#             ans = knapsack(n, w, wt, val, i + 1,dp)
#             dp[i] = ans
#         else:
#             ans = dp[i]
#     else:
#         if dp[i] == -1:
#             ans1 = val[i] + knapsack(n, w - wt[i], wt, val, i + 1,dp)
#             ans2 = knapsack(n, w, wt, val, i + 1,dp)
#             ans = max(ans1, ans2)
#             dp[i] = ans
#         else:
#             ans = dp[i]
#     return ans


n = int(input())
wt = [int(x) for x in input().split()]
val = [int(x) for x in input().split()]
w = int(input())
dp = [-1 for i in range(n+1)]
print(knapsack(n, w, wt, val, 0,dp))
