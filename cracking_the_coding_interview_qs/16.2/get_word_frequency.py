import re
def build_word_frequency(book):
    words = re.split("\W", book)
    ans = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in ans:
            ans[word_lower] += 1
        else:
            ans[word_lower] = 0
    return ans

def get_word_frequency(word, word_frequency):
    return word_frequency[word.lower()]