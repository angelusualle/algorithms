def reverse_int(n):
    s = str(n)
    if s[0] == '-':
        answer = '-' + s[1][::-1]
    else:
        answer = '' + s[::-1]
    return int(answer)