# O(n + m) time and O(n) space
def is_rotation(s1, s2):
    if len(s1) == len(s2) and s2 in ''.join([s1, s1]):
        return True
    else:
        return False


"""
# O(n + m) time where n and m are size of strings, and O(n+m) space
def is_rotation(s1, s2):
    s1_chars = {}
    for letter in s1:
        if letter not in s1_chars:
            s1_chars[letter] = 1
        else:
            s1_chars[letter] += 1
    for letter in s2:
        if letter not in s1_chars:
            return False
        if s1_chars[letter] == 0:
            return False
        s1_chars[letter] -= 1
    for letter in s1:
        if s1_chars[letter] != 0:
            return False
    pattern = ''.join([s1,s1])
    if s2 not in pattern:
        return False
    return True
"""