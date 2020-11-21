# O(nslog(s)) where n is number of words and s is length of string
def group_anagrams(arr):
    buckets = {}
    for word in arr:
        sorted_word = ''.join(sorted(word))
        if sorted_word in buckets:
            buckets[sorted_word].append(word)
        else:
            buckets[sorted_word] = [word]
    ans = []
    for key in buckets:
        for word in buckets[key]:
            ans.append(word)
    return ans