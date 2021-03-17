# O(n) time and space where n is length of s
def is_valid_parenthesis(s):
    stack = []
    for c in s:
        if c in [')', ']', '}']:
            if len(stack) == 0:
                return False
            elif c == ')' and stack[-1] != '(':
                return False
            elif c == ']' and stack[-1] != '[':
                return False
            elif c == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        return True
    else:
        return False