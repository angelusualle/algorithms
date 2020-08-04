# O(2^n) 
def generate_n_parenthesis(n):
    ans = []
    generate_n_parenthesis_recursive(n*2, 0, 0, "", ans)
    return ans

def generate_n_parenthesis_recursive(n, n_o, n_c, prefix, ans):
    if n-n_c-n_o == 0:
        ans.append(prefix)
        return
    if n_o < n // 2:
        generate_n_parenthesis_recursive(n, n_o+1, n_c, prefix + '(', ans)
    if n_c < n_o:
        generate_n_parenthesis_recursive(n, n_o, n_c + 1, prefix + ')', ans)
    