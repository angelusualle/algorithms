class Three_Stacks():
    def __init__(self):
        self.pos_refs = []
        self.pos_refs.append(0)
        self.pos_refs.append(1)
        self.pos_refs.append(2)
        self.arr = [None, None, None]
    def pop(self, stack_num):
        pos = self.pos_refs[stack_num]
        item = self.arr[pos]
        if item is not None:
            self.pos_refs[stack_num] -= 3
        return item
    def push(self, stack_num, item):
        pos = self.pos_refs[stack_num]
        pos += 3
        if pos + 1 > len(self.arr):
            self.arr.append(None)
            self.arr.append(None)
            self.arr.append(None)
        self.arr[pos] = item
        self.pos_refs[stack_num] += 3
    def peek(self, stack_num):
        return self.arr[self.pos_refs[stack_num]]