from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)


def findFirstLastPosition(arr, n, x):
    # Write your code here.
    # Return a tuple containing two integers denoting the first and last occurrence of X.
    flag = False
    FO = -1
    LO = -1
    for i in range(n):
        if arr[i] == x and flag is False:
            flag = True
            FO = i
            LO = i
        elif arr[i] == x and flag is True:
            LO = i
        elif arr[i] > x:
            break
    return FO, LO




# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    X = int(stdin.readline())
    return N, arr, X


tc = int(input())
while tc > 0:
    N, arr, X = takeInput()
    ans = findFirstLastPosition(arr, N, X)
    stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
    tc -= 1
