class My_Queue():
    def __init__(self):
        self.stack_new_first = []
        self.stack_old_first = []
    def enqueue(self, item):
        self.stack_new_first.append(item)
    def dequeue(self):
        if len(self.stack_old_first) == 0:
            while len(self.stack_new_first) > 0:
                self.stack_old_first.append(self.stack_new_first.pop())
        return self.stack_old_first.pop()