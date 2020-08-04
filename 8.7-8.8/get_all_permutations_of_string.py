# O(n!) time, O(n) space, but faster if duplicates present
def get_all_permutations_of_string_with_dups(string):
    ans = []
    char_counter = {}
    for letter in string:
        if letter in char_counter:
            char_counter[letter] += 1
        else:
            char_counter[letter] = 1
    get_all_permutations_of_arr_with_dups(list(string), "", char_counter, len(string), ans)
    return [''.join(x) for x in ans]

def get_all_permutations_of_arr_with_dups(arr, prefix, char_counter, remaining, ans):
    if remaining == 0:
        ans.append(prefix)
        return
    for k in char_counter:
        count = char_counter[k]
        if count > 0:
            char_counter[k] = count - 1
            get_all_permutations_of_arr_with_dups(arr,prefix+k, char_counter, remaining - 1, ans)
            char_counter[k] = count

# O(n!)
def get_all_permutations_of_string(string):
    ans = []
    get_all_permutations_of_arr(list(string),len(string), len(string), ans)
    return [''.join(x) for x in ans]

    
def get_all_permutations_of_arr(arr, size, n, ans):
    if (size == 1): 
        ans.append(arr[:])
        return
    for i in range(size): 
        get_all_permutations_of_arr(arr,size-1,n, ans)
        if size % 2: 
            arr[0], arr[size-1] = arr[size-1], arr[0] 
        else: 
            arr[i], arr[size-1] = arr[size-1], arr[i] 