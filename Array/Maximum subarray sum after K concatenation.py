""" https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381873
?leftPanelTab=0 """


def kadane(arr, n, k):
    curr_sum = 0
    total_sum = -1e9
    for i in range(n * k):
        curr_sum += arr[i % n]
        total_sum = max(curr_sum, total_sum)
        if curr_sum < 0:
            curr_sum = 0

    return total_sum


def maxSubSumKConcat(arr, n, k):
    # Write your code here.
    if k == 1:
        total_sum = kadane(arr, n, 1)
        return total_sum
    arr_sum = 0
    for i in arr:
        arr_sum += i
    if arr_sum <= 0:
        total_sum = kadane(arr, n, 2)
        return total_sum
    else:
        total_sum = kadane(arr, n, 2)
        total_sum += (k - 2)* arr_sum
        return total_sum


t = int(input())
while t > 0:
    n, k = [int(x) for x in input().split()[:2]]
    arr = [int(x) for x in input().split()]
    print(maxSubSumKConcat(arr, n, k))
    t -= 1
