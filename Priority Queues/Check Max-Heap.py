# Given an array of integers, check whether it represents max-heap or not. Return true if the given array represents
# max-heap, else return false .
def checkMaxHeap(lst):
    for parentIndex in range(n//2):
        childLeftIndex = 2 * parentIndex + 1
        childRightIndex = 2 * parentIndex + 2
        if lst[childLeftIndex] > lst[parentIndex]:
            return False
        if childRightIndex < len(lst) and lst[childRightIndex] > lst[parentIndex]:
            return False

    return True


# Main Code
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
