# O(n) space and time where n is num of chars
def str_to_int(s):
    result = []
    neg = None
    for c in s:
        if c == ' ' and neg is not None:
            break
        if c == ' ' and len(result) == 0:
            continue
        if c == ' ' and len(result) > 0:
            break
        if c in ['-', '+']:
            if neg is not None or len(result) > 0:
                break
            else:
                if c == '-':
                    neg = True
                else:
                    neg = False
            continue
        if not c.isdigit():
            break
        result.append(c)
    i = 0
    max_i = len(result) - 1
    answer = 0
    while i < len(result):
        answer += int(result[i])*10**(max_i - i)
        i += 1
    if neg == False or neg is None:
        pass
    else:
        answer*= -1
    if answer > 2**31 -1:
        return 2**31 -1
    if answer < -2**31:
        return -2**31
    return answer