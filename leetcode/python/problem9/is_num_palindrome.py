import math

# O(log10(n)) where n is number O(1) space
def is_num_palindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    l_digit = int(math.log10(x))
    r_digit = 0
    while r_digit < l_digit:
        if ((x % 10**(r_digit+1)) // 10**(r_digit)) != ((x % 10**(l_digit+1)) // 10**(l_digit)):
            return False
        l_digit -= 1
        r_digit += 1
    return True