# O(n) time and space complexity
def compress(string):
    last_letter = string[0]
    count = 1
    new_string = []
    for letter in string[1:]:
        if last_letter != letter:
            new_string.append(last_letter)
            new_string.append(str(count))
            last_letter = letter
            count = 1
        else:
            count += 1
    new_string.append(last_letter)
    new_string.append(str(count))
    if len(new_string) < len(string):
        return ''.join(new_string)
    else:
        return string
