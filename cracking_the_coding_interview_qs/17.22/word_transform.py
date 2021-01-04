# O(N^3) time O(1) space
def word_transform(w1, w2, cache, dictionary, t = 0):
    if w1+w2 in cache:
        return cache[w1+w2]
    if w1 == w2:
        return w2
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
    if diff == 1:
        return w2
    for i in range(t, len(w1)):
        sub = w1[0:i] + w2[i] + w1[i+1:]
        if sub in dictionary:
            path = word_transform(sub, w2, cache, dictionary, t+1)
            if path is not None:
                cache[w1+w2] = sub + '-> ' + path
                if t != 0:
                    return sub + '-> ' + path
                else:
                    return w1 + '-> ' + sub + '-> ' + path
    cache[w1+w2] = None
    return None