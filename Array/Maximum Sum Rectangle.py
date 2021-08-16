from sys import maxsize
def kadane_sum(arr):
    curr_sum = 0
    total_sum = -maxsize
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum > total_sum:
            total_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return total_sum


def maxSumRectangle(arr, n, m):
    # write your code here
    max_sum = -maxsize
    temp_arr = [0] * n
    for left in range(m):
        for i in range(n):
            temp_arr[i] = 0
        for right in range(left, m):
            for i in range(n):
                temp_arr[i] += arr[i][right]
            curr_sum = kadane_sum(temp_arr)
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum


t = int(input())
while t > 0:
    n, m = [int(x) for x in input().split()[:2]]
    arr = [[int(j) for j in input().split()] for i in range(n)]
    print(maxSumRectangle(arr, n, m))
    t -= 1
