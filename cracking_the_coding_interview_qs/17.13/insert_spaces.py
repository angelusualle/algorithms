# O(n^2) time and O(n) space through memoization
def insert_spaces(text, dictionary, cache={}):
    if not len(text):
        return (0, '')
    if text in cache:
        return cache[text]
    best = (float('inf'), None)
    for i in range(1, len(text) + 1):
        sub_sequence = text[0:i]
        if sub_sequence in dictionary:
            val, sub_text = insert_spaces(text[i:], dictionary, cache)
            if val < best[0]:
                best = (val, ' ' + sub_sequence + ' ' + sub_text)
        else:
            val = len(sub_sequence)
            val2, sub_text = insert_spaces(text[i:], dictionary, cache)
            val += val2
            if val < best[0]:
                best = (val, sub_sequence + sub_text)
    best = (best[0], best[1].replace('  ', ' '))
    cache[text] = best
    return best
            


