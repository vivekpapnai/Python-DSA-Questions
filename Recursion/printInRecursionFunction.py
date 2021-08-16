def printFact(n, ans):
    if n == 0:
        print(ans)
        return 1
    ans = n * ans
    printFact(n - 1, ans)


n = int(input())
printFact(n, 1)
