def convert_num_to_binary_representation(num):
    ans = ""
    i = 1
    remainder = num
    while remainder > 0:
        if i > 32:
            return "ERROR"
        rem = remainder - 1.0/(2**i)
        if rem >= 0:
            ans += "1"
            remainder = rem
        else:
            ans += "0"
        i += 1
    while len(ans) < 32:
        ans += "0"
    return ans
