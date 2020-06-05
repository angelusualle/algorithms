def has_unique_chars(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True