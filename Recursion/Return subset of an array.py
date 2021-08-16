# Given an integer array (of length n), find and return all the subsets of input array. Subsets are of length varying
# from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important. Input format :
#
# Line 1 : Size of array
#
# Line 2 : Array elements (separated by space)
#
# Sample Input:
# 3
# 15 20 12
# Sample Output:
# [] (this just represents an empty array, don't worry about the square brackets)
# 12
# 20
# 20 12
# 15
# 15 12
# 15 20
# 15 20 12

def returnSubset(arr):
    if len(arr) == 0:
        # output = [[]]
        return [" "]
    ans = returnSubset(arr[1:])
    frst_ele = arr[0]
    rslt = []
    for i in ans:
        rslt.append(str(i))
    for i in ans:
        rslt.append(str(frst_ele)+" " + str(i))

    return rslt


n = int(input())
arr = [int(x) for x in input().split()]
rslt = returnSubset(arr)
for i in rslt:
    print(i)