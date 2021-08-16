"""
Problem Statement
You have been given an integer array/list 'ARR' of size 'N'. Write a solution to check if it could become non-decreasing by modifying at most 1 element.
We define an array as non-decreasing, if ARR[i] <= ARR[i + 1] holds for every i (0-based) such that (0 <= i <= N - 2).
"""
"""
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381888
"""


def isNonDecreasing(arr, n):
    count = 0
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            count += 1
    if count == n - 1:
        return True
    return False


def isPossible(arr, n):
    # Write your code here.
    notInOrderIndx = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:

            if notInOrderIndx != -1: # checking if there are two index not in order
                return False
            notInOrderIndx = i

    if notInOrderIndx == 0 or notInOrderIndx == -1 or notInOrderIndx == n-2: # checking if first or last index is not in order
        return True

    if arr[notInOrderIndx -1] <= arr[notInOrderIndx + 1]:
        return True

    if arr[notInOrderIndx] <= arr[notInOrderIndx + 2]:
        return True

    return False




t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if isPossible(arr, n):
        print("true")
    else:
        print("false")
