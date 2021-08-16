"""Problem Statement You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of
the longest consecutive sequence. The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ...,
'NUM' + L] where 'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence. """

"""
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381889?leftPanelTab=0
"""


def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    arr.sort()
    curr_ele = arr[0]
    consecutive_sequence = 1
    longest_sequence = 1
    for i in range(1, n):
        if arr[i - 1] == arr[i] - 1:
            consecutive_sequence += 1
            if consecutive_sequence > longest_sequence:
                longest_sequence = consecutive_sequence
        elif arr[i - 1] == arr[i]:
            continue
        else:
            consecutive_sequence = 1
    if consecutive_sequence > longest_sequence:
        longest_sequence = consecutive_sequence
    return longest_sequence


"""
above code will have nlogn time complexity 
"""





t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(lengthOfLongestConsecutiveSequence(arr, n))


