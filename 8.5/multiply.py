# O(log(s)) where s is smaller value of two
def multiply(num1,  num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == 1:
        return num2
    if num2 == 1:
        return num1
    bigger = num1
    smaller= num2
    if num1 < num2:
        smaller = num1
        bigger = num2
    s = smaller >> 1
    half = multiply(s, bigger)
    if smaller % 2 == 0:
        return half + half
    else:
        return half + half + bigger

"""
# O(N) where n is num1 number O(N) space
def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == 1:
        return num2
    if num2 == 1:
        return num1
    return num2 + multiply(num1-1, num2)
"""