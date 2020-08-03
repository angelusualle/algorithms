from copy import deepcopy

# O(n*2^n) space and time
def get_all_possible_subsets(nums):
    if len(nums) == 0:
        s = set()
        return [s]
    new_num = nums.pop()
    possibilites = get_all_possible_subsets(nums)
    new_possibilities = deepcopy(possibilites)
    for pos in new_possibilities:
        pos.add(new_num)
    possibilites.extend(new_possibilities)
    return possibilites
