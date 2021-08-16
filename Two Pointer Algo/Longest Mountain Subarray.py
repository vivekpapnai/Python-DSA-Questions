"""You are given an array of 'N' integers denoting the heights of the mountains. You need to find the length of the
longest subarray which has the shape of a mountain. A mountain subarray is defined as a subarray which consists of
elements that are initially in ascending order until a peak element is reached and beyond the peak element all other
elements of the subarray are in decreasing order. """

"""
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118509/offering/1376554
"""


# def isMountain(arr):
#     i = 0
#     n = len(arr)
#     j = n - 1
#     mid = (i + j) // 2
#     while i <= j:
#         if not (i <= mid and j <= mid):
#             return False
#         i += 1
#         j -= 1
#     return True


def longestMountain(arr, n):
    maxCount = 0
    start = -1
    end = -1
    if n < 3:
        return 0
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            if end != -1:
                start = -1
                end = -1
            if start == -1:
                start = i
        else:
            if arr[i] > arr[i + 1]:
                if start != -1:
                    end = i + 1
                if end != -1 and start != -1:
                    maxCount = max(maxCount, end - start + 1)
            else:
                start = -1
                end = -1
    if end != -1 and start != -1:
        maxCount = max(maxCount, end - start + 1)

    return maxCount

    return maxCount


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(longestMountain(arr, n))
