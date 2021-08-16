def leftRotate(strr, d):
    # Write your code here.
    while d > len(strr):
        d = d - len(strr)

    temp = strr[:d]
    resultStr = strr[d:] + temp

    return resultStr


def rightRotate(strr, d):
    # Write your code here.
    while d > len(strr):
        d = d - len(strr)
    resultstr = ""
    resultstr += strr[len(strr)-d:len(strr)]
    resultstr += strr[:len(strr) -d]

    return resultstr


t = int(input())
for i in range(t):
    strr = input()
    d = int(input())
    print(leftRotate(strr, d))
    print(rightRotate(strr, d))
