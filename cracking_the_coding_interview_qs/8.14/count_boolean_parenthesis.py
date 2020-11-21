def count_boolean_parenthesis(string, result, cache={}):
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return int(string) == int(result)
    if (str(result) + string) in cache:
        return cache[str(result) + string]
    ways = 0
    for i in range(1, len(string), 2):
        c = string[i]
        left = string[0:i]
        right = string[i+1:]
        left_true = count_boolean_parenthesis(left, True, cache)
        left_false = count_boolean_parenthesis(left, False, cache)
        right_true = count_boolean_parenthesis(right, True, cache)
        right_false = count_boolean_parenthesis(right, False, cache)
        total = (left_true + left_false) * (right_true + right_false)
        total_true = 0
        if (c == '^'):
            total_true = left_true * right_false + left_false*right_true
        elif (c == '&'):
            total_true = left_true*right_true
        elif (c == '|'):
            total_true = left_true * right_true + left_false * right_true + left_true * right_false
        sub_ways = -1
        if result:
            sub_ways = total_true
        else:
            sub_ways = total - total_true
        ways += sub_ways
    cache[str(result) + string] = ways
    return ways