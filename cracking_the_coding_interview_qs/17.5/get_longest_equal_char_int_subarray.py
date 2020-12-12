# O(N) time and space
def get_longest_equal_char_int_subarray(arr):
    best_len = 0
    best_start_index = 0
    best_end_index = 0
    num_letters = 0
    num_nums = 0
    mem = {}
    for i,digit in enumerate(arr):
        if type(digit) is int:
            num_nums += 1
            z = 1
        else:
            num_letters += 1
            z = -1
        diff = num_letters - num_nums
        if diff in mem:
            len_ = i - mem[diff]
            if len_ > best_len:
                best_start_index = mem[diff]
                best_end_index = i
        diff += z
        if diff not in mem:
            mem[diff] = i
    return arr[best_start_index:best_end_index+1]

        