import sys


def minArray(arr, mini):
    if len(arr) == 0:
        print(mini)
        return
    mini = min(mini, arr[0])
    minArray(arr[1:], mini)


array = [5, 7, 11, -32, 9, 4]
minArray(array, sys.maxsize)
