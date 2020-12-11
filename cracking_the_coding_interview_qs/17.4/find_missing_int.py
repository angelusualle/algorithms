# O(n) if only accessing 1 bit possible at a time
def find_missing_int(nums, n):
    ans = []
    candidates = {x:x for x in nums}
    delete = []
    while candidates:
        ones = 0
        zeros = 0
        zero_l = []
        ones_l = []
        for c in candidates:
            digit = candidates[c] & 1
            if digit:
                ones += 1
                ones_l.append(c)
            else:
                zeros += 1
                zero_l.append(c)
            candidates[c] >>= 1
        if len(candidates) % 2:
            if ones < zeros:
                ans.append(1)
            elif ones > zeros:
                ans.append(0)
        else:
            if ones == zeros:
                ans.append(0)
            elif ones < zeros - 1:
                ans.append(1)
        if ans[-1] == 0:
            for d in ones_l:
                del candidates[d]
        elif ans[-1] == 1:
            for d in zero_l:
                del candidates[d]
    true_ans = 0
    while ans:
        true_ans = (true_ans << 1) | ans.pop()
    return true_ans


'''
# O(n) if only we could get num at once
def find_missing_int(nums, n):
    target = n*(n + 1) / 2
    return target - sum(nums)
'''