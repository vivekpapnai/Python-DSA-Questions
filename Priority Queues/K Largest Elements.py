# You are given with an integer k and an array of integers that contain numbers in random order. Write a program to
# find k largest numbers from given array. You need to save them in an array and return it. Time complexity should be
# O(nlogk) and space complexity should be not more than O(k).

import heapq


def kLargest(lst, k):
    li = lst[:k]
    heapq.heapify(li)
    n = len(lst)
    for i in range(k, n):
        if li[0] < lst[i]:
            heapq.heapreplace(li, lst[i])
    return li


# Main Code
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = kLargest(lst, k)
print()
