def regex_match(s,p):
    return _regex_match(s,p,0,0)

def _regex_match(s, p, i, j):
    while i < len(s) or j < len(p):
        if j >= len(p):
            return False
        if i >= len(s) and not (j + 1 < len(p) and p[j+1] == '*'):
            return False
        elif p[j] not in ['.', '*'] and not (j + 1 < len(p) and p[j+1] == '*'):
            if p[j] == s[i]:
                j += 1
                i += 1
            else:
                return False
        elif p[j] == '.' and not (j + 1 < len(p) and p[j+1] == '*'):
            j += 1
            i += 1
        elif j + 1 < len(p) and p[j+1] == '*':
            if p[j] != '.':
                let = p[j]
                y = i
                if _regex_match(s,p,i,j+2):
                    return True
                if y < len(s):
                    while let == s[y]:
                        if _regex_match(s,p,y+1,j+2):
                            return True
                        y += 1
                        if y >= len(s):
                            break
                return False
            else:
                for ij in range(0, len(s) - i +1):
                    if _regex_match(s,p,i+ij,j+2):
                        return True
                return False
    return True