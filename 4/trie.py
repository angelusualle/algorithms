class Node():
    def __init__(self, root=False, letter=None, complete=False):
        self.root = root
        self.letter = letter
        self.complete = complete
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node(root=True)
    def add_word(self, word):
        node = self.root
        for i,let in enumerate(word):
            if let in node.children:
                node = node.children[let]
            else:
                node.children[let] = Node(letter=let)
                if i < len(word) -1:
                    node = node.children[let]
        node.children[let].complete = True
    def valid_prefix(self, word):
        node = self.root
        for let in word:
            if let not in node.children:
                return False
            node = node.children[let]
        return True