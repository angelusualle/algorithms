# O(ns) where n is number of strings and s is size of shortest string
def longest_common_prefix(strs):
    if len(strs) == 0 or len(strs[0]) == 0:
        return ""
    i = 0
    while True:
        for s in strs:
            if i >= len(s):
                return s[0:i]
            if s[i] != strs[0][i]:
                return s[0:i]
        i += 1