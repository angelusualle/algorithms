# run time complexity is O(n) where n is size of shortest string
# space complexity is O(1)
def are_not_at_most_one_edit_away(str1, str2):
    errors = 0
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            errors += 1
            if errors > 1:
                return False
            if len(str1) > len(str2):
                i += 1
            elif len(str2) > len(str1):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    while i < len(str1):
        errors += 1
        i += 1
        if errors > 1:
            return False
    while j < len(str2):
        errors += 1
        j += 1
        if errors > 1:
            return False
    return True