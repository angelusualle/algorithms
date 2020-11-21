# O(n)
def has_unique_chars(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

# O(nlog(n)) w/o data structures
""" def has_unique_chars(s):
    s = sorted(s)
    for i, c in enumerate(s):
        if i > 0 and c == s[i-1]:
            return False
    return True """
