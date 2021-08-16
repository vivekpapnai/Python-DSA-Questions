from sys import stdin

def possibleToMakeTriangle(arr):

    arr = sorted(arr)
    for i in range(len(arr)-2):
        a = arr[i]
        b = arr[i+1]
        c = arr[i+2]
        if a + b > c and a + c > b and b + c > a:
            return True
    return False

# Main code.
t = int(input().strip())

for i in range(t):
    n = list(map(int, stdin.readline().strip().split(" ")))

    if len(n) > 1:
        arr = n
    else:
        arr = list(map(int, stdin.readline().strip().split(" ")))

    if (possibleToMakeTriangle(arr)):
        print("YES")
    else:
        print("NO")
