# Given an array A of random integers and an integer k, find and return the kth largest element in the array.
# Note: Try to do this question in less than O(N * logN) time.

import heapq


def kthLargest(lst, k):
    li = lst[:k]
    heapq.heapify(li)
    n = len(lst)
    for i in range(k, n):
        if lst[i] > li[0]:
            heapq.heapreplace(li, lst[i])
    return li[-k]


# Main
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = kthLargest(lst, k)
print(ans)
