class Number_Pad_To_Words():
    let_to_num = {
        'a': '2',
        'b': '2',
        'c': '2',
        'd': '3',
        'e': '3',
        'f': '3',
        'g': '4',
        'h': '4',
        'i': '4',
        'j': '5',
        'k': '5',
        'l': '5',
        'm': '6',
        'n': '6',
        'o': '6',
        'p': '7',
        'q': '7',
        'r': '7',
        's': '7',
        't': '8',
        'u': '8',
        'v': '8',
        'w': '9',
        'x': '9',
        'y': '9',
        'z': '9'
    }
    # O(ns) n -> number of words, s -> num of letters
    def __init__(self, words):
        self.num_to_words = {}
        for word in words:
            ans = ''
            for let in word:
                ans+= self.let_to_num[let]
            if ans not in self.num_to_words:
                self.num_to_words[ans] = [word]
            else:
                self.num_to_words[ans].append(word)
    
    # O(1) lookup time
    def get_num_to_words(self, num):
        if str(num) not in self.num_to_words:
            return []
        return self.num_to_words[str(num)]