"""You have been given an integer array/list (ARR) of size N. You have to return an array/list PRODUCT such that
PRODUCT[i] is equal to the product of all the elements of ARR except ARR[i]

link : https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381866
"""

from sys import stdin


def getProductArrayExceptSelf(arr, n):
    """ we can approach this in brute force but the time complexity will be n^2 so to overcome this we will use prefix
    sum array and suffix sum array """
    pre_prod = [1] * (n)
    suf_prod = [1] * (n)
    for i in range(1, n):
        prod = pre_prod[i - 1] * arr[i - 1]
        pre_prod[i] = prod
    # return pre_prod
    for i in range(n - 2, -1, -1):
        prod = suf_prod[i + 1] * arr[i + 1]
        suf_prod[i] = prod
    rslt_arr = [1] * n
    for i in range(n):
        prod = suf_prod[i]*pre_prod[i]
        rslt_arr[i] = prod
    return rslt_arr


def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    product = getProductArrayExceptSelf(arr, n)
    printList(product, n)

    t -= 1
