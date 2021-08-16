from sys import stdin


def getProductArrayExceptSelf(arr, n):
    mod = (10 ** 9) + 7
    pre_mul = ([1] * n)
    for i in range(1, n):
        pre_mul[i] = (arr[i - 1] * pre_mul[i - 1]) % mod
    suf_mul = [1] * n
    for i in range(n - 2, -1, -1):
        suf_mul[i] = (arr[i + 1] * suf_mul[i + 1]) % mod
    for i in range(n):
        arr[i] = pre_mul[i]*suf_mul[i]
    return arr


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
