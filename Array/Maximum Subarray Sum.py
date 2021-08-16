# using kadane's algorithm
""" https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381870 """
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def maxSubarraySum(arr, n):
    if len(arr) > 0:
        max_sum = arr[0]
        curr_sum = arr[0]
    else:
        return 0
    for i in range(1, n):
        if arr[i] + curr_sum > arr[i]:
            curr_sum += arr[i]
        else:
            curr_sum = arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


# taking inpit using fast I/O
def takeInput():
    n = int(input())

    if (n == 0):
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


# main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
