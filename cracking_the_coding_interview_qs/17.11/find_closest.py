# O(A + B) where A, B are number of occurences of each word.
def find_closest(word1, word2, pre_computed_word_to_position):
    i = 0
    j = 0
    best = float('inf')
    while i < len(pre_computed_word_to_position[word1]) and j < len(pre_computed_word_to_position[word2]):
        w1_loc = pre_computed_word_to_position[word1][i]
        w2_loc = pre_computed_word_to_position[word2][j]
        len_ = abs(w2_loc - w1_loc)
        if len_ < best:
            best = len_
        if w1_loc < w2_loc:
            i += 1
        else:
            j += 1
    return best

# O(N) to build
def precomute_word_to_position(words):
    ans = {}
    for i, word in enumerate(words):
        if word not in ans:
            ans[word] = [i]
        else:
            ans[word].append(i)
    return ans