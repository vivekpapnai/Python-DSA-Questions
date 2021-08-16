"""You are given an array Arr consisting of n integers, you need to find all the distinct triplets present in the
array which adds up to zero. An array is said to have a triplet {arr[i], arr[j], arr[k]} with 0 sum if there exists
three indices i, j and k such that i!=j, j!=k and i!=k and arr[i] + arr[j] + arr[k] = 0. """

"""
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118509/offering/1376555?leftPanelTab=0
"""

from sys import stdin, stdout, setrecursionlimit


def findTriplets(arr, n):
    # Write your code here
    # Return a list of triplets
    ans = []
    arr = sorted(arr)
    i = 0
    while i < n:
        front = i + 1
        back = n - 1
        target = -arr[i]
        while front < back:
            sum = arr[front] + arr[back]
            if sum > target:
                back -= 1
            elif sum < target:
                front += 1
            else:
                x = arr[front]
                y = arr[back]
                temp = [arr[i], x, y]
                ans.append(temp)
                while front < back and arr[front] == x:
                    front += 1
                while front < back and arr[back] == y:
                    back -= 1
        while i+1 < n and arr[i] == arr[i+1]:
            i += 1
        i += 1
    return ans

# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = findTriplets(arr, N)
    temp = [-1, -1, -1]
    if len(ans) == 0:
        stdout.write("-1\n")
    else:
        for i in ans:
            i.sort()
            if temp != i:
                stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
                temp = i
    tc -= 1
