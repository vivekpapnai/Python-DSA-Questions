def search(arr, target):
    # Write your code here
    si = 0
    ei = len(arr)-1
    while si <= ei:
        mid = (si + ei)//2
        if arr[mid] == target: # if element found
            return  mid

        elif arr[mid] >= arr[si]: # if left side is sorted
            if arr[si] <= target <= arr[mid]: # checking if target lies in the range
                ei = mid - 1
            else:
                si = mid + 1
        else:  # if right side is sorted
            if arr[ei] >= target > arr[mid]:
                si = mid + 1
            else:
                ei = mid - 1

    return -1  # if element is not found
