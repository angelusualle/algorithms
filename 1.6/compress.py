# O(n) time and space complexity
def compress(string):
    last_letter = string[0]
    count = 1
    new_string = ''
    for letter in string[1:]:
        if last_letter != letter:
            new_string += last_letter + str(count)
            last_letter = letter
            count = 1
        else:
            count += 1
    new_string += last_letter + str(count)
    if len(new_string) < len(string):
        return new_string
    else:
        return string
