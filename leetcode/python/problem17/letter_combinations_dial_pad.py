# O(3.11^n) where n is number of digits
def letter_combinations_dial_pad(digits):
    digit_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    combos = []
    for d in digits:
        if len(combos) == 0:
            for di in digit_map[d]:
                combos.append(di)
        else:
            new_combos = []
            for di in digit_map[d]:
                for c in combos:
                    new_combos.append(c + di)
            combos = new_combos
    return combos