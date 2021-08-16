def partition(arr, si, ei, start, mid):
    end = ei
    pivot = arr[ei]
    while mid[0] <= end:
        if arr[mid[0]] < pivot:
            arr[start[0]], arr[mid[0]] = arr[mid[0]], arr[start[0]]
            start[0] += 1
            mid[0] += 1
        elif arr[mid[0]] > pivot:
            arr[end], arr[mid[0]] = arr[mid[0]], arr[end]
            end -= 1
        else:
            mid[0] += 1


def quickSort(arr, si, ei):
    if si >= ei:
        return
    if si + 1 == ei:
        if arr[si] > arr[ei]:
            arr[si], arr[ei] = arr[ei], arr[si]
            return

    start = [si]
    mid = [si]
    partition(arr, si, ei, start, mid)
    quickSort(arr, si, start[0] - 1)
    quickSort(arr, mid[0], ei)

    return


def quickSortUsingDutchNationalFlag(arr):
    ei = len(arr)
    quickSort(arr, 0, ei - 1)
    return


arr = [int(x) for x in input().split()]
quickSortUsingDutchNationalFlag(arr)
for i in arr:
    print(i, end=" ")