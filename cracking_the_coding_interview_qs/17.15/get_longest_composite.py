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
    if self_ok and word in word_set:
        cache[word] = True
        return True
    for i in range(1, len(word)):
        l = word[:i]
        if l not in word_set:
            continue
        r = word[i:]
        if is_composite(r, word_set, cache, self_ok=True):
            cache[word] = True
            return True
    cache[word] = False
    return False
