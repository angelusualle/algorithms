# O(4^n/sqrt(n)) where n is num of parenthesis
def gen_parenthesis(prefix, n_open, len_tar, ans):
    if len(prefix) == len_tar:
        if n_open == 0:
            ans.append(''.join(prefix))
        return
    if n_open > 0:
        new = prefix[:]
        new.append(')')
        gen_parenthesis(new, n_open-1, len_tar, ans)
    new = prefix[:]
    new.append('(')
    gen_parenthesis(new, n_open + 1, len_tar, ans)