"""https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381864?leftPanelTab=0
"""
def xorQuery(queries):
    # Write your code here.
    arr = []
    xor_array = [0]*10001
    for i in queries:
        var = i[0]
        value = i[1]
        if var == 1:
            arr.append(value)
        else:
            xor_array[i] ^= value
            xor_array[len(queries)] ^= value
    # here we are appending the values in xor_Array at index of len of array and then we are doing xor operation for
    # before that index in array
    for i in range(len(arr)):
        if i == 0:
            arr[i] ^= xor_array[i]
        else:
            xor_array[i] = xor_array[i] ^ xor_array[i-1]
            arr[i] ^= xor_array[i]
    return arr

def xorQueryBest(queries):
    # Write your code here.
    arr = []
    flag = 0
    for i in range(len(queries)):
        var = queries[i][0]
        value = queries[i][1]
        if var == 1:
            arr.append(value^flag)
        else:
            flag = flag ^ value
    for i in range(len(arr)):
        arr[i] = arr[i] ^ flag
    return arr