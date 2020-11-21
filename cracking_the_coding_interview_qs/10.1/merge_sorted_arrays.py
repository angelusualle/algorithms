def merge_sorted_arrays(arr1, arr2):
    ans = arr1[:]
    ans.extend(arr2)
    i = 0
    j = 0
    z = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans[z] = arr1[i]
            i += 1
            z += 1
        else:
            ans[z] = arr2[j]
            j += 1
            z += 1
    if i < len(arr1):
        ans[z] = arr1[i]
        i += 1
        z += 1
    return ans