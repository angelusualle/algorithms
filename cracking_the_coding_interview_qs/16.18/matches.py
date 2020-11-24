# O(n^2) time and O(n) space by string size
def matches(pat, val):
    first_p = pat[0]
    if first_p == 'a':
        second_p = 'b'
    num_first = 0
    num_second = 0
    for let in pat:
        if let == first_p:
            num_first += 1
        else:
            num_second += 1
    max_first_size = len(val) // num_first
    for size_first in range(1, max_first_size + 1):
        size_second = (len(val) - size_first*num_first) // num_second
        if size_first*num_first + size_second*num_second == len(val):
            first = val[:size_first]
            second = val[pat.index(second_p)*size_first:pat.index(second_p)*size_first + size_second]
            projection = ''
            for let in pat:
                if let == first_p:
                    projection = ''.join([projection, first])
                else:
                    projection = ''.join([projection, second])
            if projection == val:
                return True
    return False
