def printFrequencyK(str, k):
    words = str.split()
    dic = {}
    for i in words:
        dic[i] = dic.get(i, 0) + 1
    for i in dic:
        if dic[i] == k:
            print(i)


s = input()
k = int(input())
printFrequencyK(s, k)
