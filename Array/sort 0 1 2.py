# You have been given an integer array/list(ARR) of size 'N'. It only contains 0s, 1s and 2s. Write a solution to
# sort this array/list.

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def sort012(arr, n):
    # write your code here
    # don't return anything
    low = 0
    mid = 0
    high = n - 1
    while high >= mid:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

        # taking input using fast I/O
    return

def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main

t = int(input().strip())
for i in range(t):
    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
