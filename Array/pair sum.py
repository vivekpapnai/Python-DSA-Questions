""" heelo"""

from sys import stdin


def pairSum(arr, S):
    li = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == S:
                sub_arr = [arr[i], arr[j]]
                li.append(sub_arr)
    return li


# Main Code
n, S = list(map(int, stdin.readline().strip().split(" ")))
arr = list(map(int, stdin.readline().strip().split(" ")))
res = pairSum(arr, S)

for ele in res:
    print(*ele)
