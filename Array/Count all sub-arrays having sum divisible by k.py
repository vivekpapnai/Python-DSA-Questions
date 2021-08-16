""" https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381869
?leftPanelTab=0 """
def subArrayCount(arr, k):
    # Write your code here.
    # Return count of all the subarray that have sum is divisible by 'k'.
    count = 0
    rem_dict = {0: 1}
    sum = 0
    rem = 0
    for i in range(len(arr)):
        sum += arr[i]
        rem = sum % k
        if rem < 0:
            rem += k
        if rem in rem_dict:
            count += rem_dict[rem]
            rem_dict[rem] += 1
        else:
            rem_dict[rem] = 1

    return count


t = int(input())
while t > 0:
    n, k = [int(x) for x in input().split()[:2]]
    arr = [int(x) for x in input().split()]
    print(subArrayCount(arr, k))
    t -= 1
