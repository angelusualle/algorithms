# O(n!) removing
def get_all_permutations_of_string_with_dups(string):
    ans = []
    get_all_permutations_of_arr(list(string),len(string), len(string), ans)
    set_data = set([''.join(x) for x in ans])
    print(set_data)
    return list(set_data)

# O(n!)
def get_all_permutations_of_string(string):
    ans = []
    get_all_permutations_of_arr(list(string),len(string), len(string), ans)
    return [''.join(x) for x in ans]
def get_all_permutations_of_arr(arr, size, n, ans):
    if (size == 1): 
        ans.append(arr)
        return
    for i in range(size): 
        get_all_permutations_of_arr(arr[:],size-1,n, ans)
        if size % 2: 
            arr[0], arr[size-1] = arr[size-1], arr[0] 
        else: 
            arr[i], arr[size-1] = arr[size-1], arr[i] 