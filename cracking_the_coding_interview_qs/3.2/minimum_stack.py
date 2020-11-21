# O(n) minimum, push, pop functions
class Minimum_Stack():
    def __init__(self):
        self.arr = []
        self.mins = []
    def push(self, item):
        self.arr.append(item)
        if len(self.mins) == 0:
            self.mins.append(item)
        else:
            self.mins.append(min(self.mins[-1], item))
    def pop(self):
        self.mins.pop()
        return self.arr.pop()
    def min(self):
        return self.mins[-1]