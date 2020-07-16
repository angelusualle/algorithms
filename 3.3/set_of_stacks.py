class Set_Of_Stacks():
    def __init__(self, max_size):
        self.max_size= max_size
        self.set = []
        self.set.append([])
        self.active_set = 0
    def push(self, item):
        if len(self.set[self.active_set]) >= self.max_size:
            self.active_set += 1
            if len(self.set) < self.active_set + 1:
                self.set.append([])
        self.set[self.active_set].append(item)
    def pop(self):
        item = self.set[self.active_set].pop()
        while len(self.set[self.active_set]) == 0 and self.active_set > 0:
            self.active_set -= 1
        return item
    def pop_at(self, i):
        if i < len(self.set) and not len(self.set[i]):
            return None
        if i == self.active_set:
            return self.pop()
        return self.set[i].pop()