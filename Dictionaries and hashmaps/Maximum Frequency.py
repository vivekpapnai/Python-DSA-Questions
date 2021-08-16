def maxFrequency(arr, n):
    dic = {}
    for i in arr:
        dic[i] = dic.get(i, 0) + 1
    # print(dic)
    max_val = 0
    for i in dic:
        if dic[i] > max_val:
            max_val = dic[i]
            max_key = i
    return max_key


n = int(input())
arr = [int(x) for x in input().split()]
print(maxFrequency(arr, n))
# maxFrequency(arr, n)
