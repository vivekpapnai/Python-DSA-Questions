"""You are given two arrays of integers. Let's call the first array A and the second array B. A finds the number of
elements in array B that are smaller than or equal to that element for every array element. """

import bisect


def countSmallerOrEqual(a, b, n, m):
    #  Write your code here
    arr = []
    b.sort()
    for i in range(n):
        if a[i] >= b[m - 1]:
            arr.append(m)
        else:
            index = bisect.bisect_right(b, a[i])
            arr.append(index)
    return arr
