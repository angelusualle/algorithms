def heap_permutation(arr, size, n, ans): 
    if (size == 1): 
        ans.append(arr)
    for i in range(size): 
        heap_permutation(arr[:],size-1,n, ans)
        if size % 2: 
            arr[0], arr[size-1] = arr[size-1], arr[0] 
        else: 
            arr[i], arr[size-1] = arr[size-1], arr[i] 