from sys import stdin


def pairSum0(l, n):
    # Write your code
    dic = {}
    count = 0
    for i in l:
        dic[i] = dic.get(i, 0) + 1
    for i in dic:
        if i > 0 and -i in dic:
            count += (dic[i]*dic[-i])
        if i == 0:
            count += (dic[i]*(dic[i]-1))//2


    return count


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(pairSum0(arr, n))
