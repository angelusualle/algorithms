def get_longest_composite(words):
    words.sort(key= lambda x: len(x), reverse=True)
    cache = {}
    word_set = set(words)
    for word in words:
        if is_composite(word, word_set, cache, self_ok=False):
            return word
    return None

def is_composite(word, word_set, cache, self_ok):
    if word in cache:
        return cache[word]
    for i in range(1, len(word)):
        l = word[:i]
        if l not in word_set:
            continue
        r = word[i:]
        if r in word_set:
            cache[word] = True
            return True
    cache[word] = False
    return False
