

def add(num1, num2):
    ans = []
    carry = 0
    while num1 != 0 and num2 != 0:
        b1 = num1 & 1
        b2 = num2 & 1
        if num1 != 0:
            num1 >>= 1
        if num2 != 0:
            num2 >>= 1
        if b1 + b2 + carry == 0:
            ans.append(0)
            carry = 0
        elif b1 + b2 + carry == 1:
            ans.append(1)
            carry = 0
        elif b1 + b2 + carry == 2:
            ans.append(0)
            carry = 1
        else:
            ans.append(1)
            carry = 1
    if carry:
        ans.append(1)
    true_ans = 0
    while ans:
        true_ans = (true_ans << 1) | ans.pop()
    return true_ans