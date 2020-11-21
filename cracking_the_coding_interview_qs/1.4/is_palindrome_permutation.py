# O(n) runtime complexity, O(1) space complexity
def is_palindrome_permutation(string):
    letter_count = {}
    string = str.lower(string)
    for letter in string:
        if not str.isalpha(letter):
            continue
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    has_odd_count = False
    for letter in letter_count:
        if letter_count[letter] %2 != 0:
            if has_odd_count:
                return False
            else:
                has_odd_count = True
    return True