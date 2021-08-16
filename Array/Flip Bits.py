""" https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381872 """


def flipBits(arr, n):
    # Write your code here
    # flag = True
    total_ones = 0
    total_max = 0
    curr_max = 0
    for i in range(n):
        if arr[i] == 1:
            total_ones += 1
        var = 0
        if arr[i] == 1:
            var = -1
        else:
            var = 1
        curr_max = max(var, curr_max + var)
        total_max = max(curr_max, total_max)
    total_max += total_ones

    return total_max


t = int(input())
while t > 0:
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(flipBits(arr, n))
    t -= 1
