class Trie():
    class Node():
        def __init__(self):
            self.term = False
            self.letter = None
            self.children = {}

    def __init__(self, strings):
        self.head = {}
        for string in strings:
            let = string[0]
            if let not in self.head:
                self.head[let] = Trie.Node()
            next_one = self.head[let]
            if len(string) < 2:
                next_one.term = True
                continue
            for i in range(1, len(string)):
                let = string[i]
                if let not in next_one.children:
                    next_one.children[let] = Trie.Node()
                next_one = next_one.children[let]
            next_one.term = True

def check_substrings_in_long_string(long, substrings):
    trie = Trie(substrings)
    ans = set()
    for i in range(len(long)):
        if long[i] not in trie.head:
            continue
        next_one = trie.head[long[i]]
        j = i + 1
        letters = [long[i]]
        while j < len(long):
            if next_one.term:
                ans.add(''.join(letters))
            let = long[j]
            if let in next_one.children:
                next_one = next_one.children[let]
            else:
                break
            letters.append(let)
            j += 1
        if next_one.term:
            ans.add(''.join(letters))
    return ans