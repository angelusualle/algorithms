# O(n^2) where n is number of chars in string
def get_longest_palindrome(s):
    best_start = 0
    best_end = 0
    for i,c in enumerate(s):
        y = i
        z = i
        y,z = expand(y,z,s)
        if y - z > best_end - best_start:
            best_start = z
            best_end = y
        y = i + 1
        z = i
        y,z = expand(y,z,s)
        if y -z > best_end - best_start:
            best_start = z
            best_end = y
    return s[best_start:best_end+1]

def expand(y,z,s):
    while y < len(s) and z >= 0:
        if s[y] == s[z]:
            y += 1
            z -= 1
        else:
            break
    y -= 1
    z += 1
    return y, z