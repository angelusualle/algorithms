from copy import deepcopy

# does in O(n) time and O(1) space (in place) where n is number of elements
def rotate_arr_90_deg(arr):
    n = len(arr)
    rotate_layer(arr, n)
    return arr

def rotate_layer(arr, n):
    if n <= 1:
        return
    for x in range(n - 1):
        val = arr[0][x]
        tmp = arr[x][-1] 
        arr[x][-1] = val 
        val = tmp
        tmp = arr[-1][-(x + 1)] 
        arr[-1][-(x + 1)] = val
        val = tmp
        tmp = arr[-(x + 1)][0]
        arr[-(x + 1)][0] = val
        val = tmp
        arr[0][x] = val
    if n == 2:
        return
    rotate_layer([x[1:-1] for x in arr], n - 2)

"""
# does in O(n) time and O(n) space not in place where n is number of elements
def rotate_arr_90_deg(arr):
    n = len(arr)
    new_arr = [[-1]* n]
    for i in range(n - 1):
        new_arr.append(deepcopy(new_arr[0]))
    for row_num, row in enumerate(arr):
        for col_num, val in enumerate(row):
            new_arr[col_num][(row_num + 1)*-1] = val
    return new_arr
"""