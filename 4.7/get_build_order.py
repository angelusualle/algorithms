#O(n) complexity
def get_build_order(deps):
    ans = []
    next_ones = [x for x in deps if len(deps[x]) == 0]
    for key in next_ones:
        del deps[key]
    while len(next_ones) > 0:
        item = next_ones.pop()
        ans.append(item)
        for key in deps:
            if item in deps[key]:
                deps[key].remove(item)
        new_next_ones = [x for x in deps if len(deps[x]) == 0]
        for key in new_next_ones:
            del deps[key]
        next_ones.extend(new_next_ones)
    if len(deps) > 0:
        return None
    return ans