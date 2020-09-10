def multiply(num1, num2):
    if num1 > 0 and num2 > 0:
        neg = False
    elif num1 < 0 and num2 < 0:
        neg = False
    else:
        neg = True
    ans = 0
    for i in range(num2):
        ans += num1
    if neg:
        actual = 0
        for i in range(ans):
            actual + -1
        ans = actual
    return ans

def subtract(num1, num2):
    return num1 + (-num2)

def divide(num1, num2):
    if num1 > 0 and num2 > 0:
        neg = False
    elif num1 < 0 and num2 < 0:
        neg = False
    else:
        neg = True
    ans = 0
    container = 0
    while container < num1:
        ans += 1
        container += num2
    if neg:
        actual = 0
        for i in range(ans):
            actual + -1
        ans = actual
    return ans