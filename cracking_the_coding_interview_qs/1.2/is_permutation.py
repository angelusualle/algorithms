
# O(a + b) time O(a) space
def is_permutation(s1,s2):
    if not len(s1) or not len(s2) or len(s1) != len(s2):
        return False
    chars_to_match = {}
    for c in s1:
        if c in chars_to_match:
            chars_to_match[c] += 1
        else:
            chars_to_match[c] = 1
    for c in s2:
        if c not in chars_to_match or not chars_to_match[c]:
            return False
        else:
            chars_to_match[c] -= 1
    return True

"""
# O(alog(a) + blog(b)) time O(1) space
def is_permutation(s1,s2):
    if not len(s1) or not len(s2) or len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i,s in enumerate(s1):
        if s != s2[i]:
            return False
    return True
"""