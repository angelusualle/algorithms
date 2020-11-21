class Min_Heap():
    def __init__(self):
        self.arr = []
    def insert(self, data):
        self.arr.append(data)
        if len(self.arr) == 0:
            return
        i = len(self.arr) - 1
        while (i-1)// 2 >= 0 and self.arr[(i-1)// 2] > self.arr[i]:
            tmp = self.arr[(i-1)//2]
            self.arr[(i-1)//2] = self.arr[i]
            self.arr[i] = tmp
            i = (i-1)//2
    def extract_min(self):
        min_val = self.arr[0]
        last_val = self.arr.pop()
        self.arr[0] = last_val
        i = 0
        while 2*i + 1 < len(self.arr):
            if self.arr[i] > self.arr[(2*i + 1)]:
                if 2*i +2 < len(self.arr) and self.arr[i] > self.arr[(2*i+2)]:
                    right_smaller = self.arr[(2*i+2)] < self.arr[(2*i + 1)]
                    if right_smaller:
                        tmp = self.arr[(2*i+2)]
                        self.arr[(2*i+2)] = self.arr[i]
                        self.arr[i] = tmp
                        i = 2*i+2
                    else:
                        tmp = self.arr[(2*i+1)]
                        self.arr[(2*i+1)] = self.arr[i]
                        self.arr[i] = tmp
                        i = 2*i+1
                else:
                    tmp = self.arr[(2*i+1)]
                    self.arr[(2*i+1)] = self.arr[i]
                    self.arr[i] = tmp
                    i = 2*i+1
            elif 2*i +2 < len(self.arr) and self.arr[i] > self.arr[(2*i + 2)]:
                tmp = self.arr[(2*i+2)]
                self.arr[(2*i+2)] = self.arr[i]
                self.arr[i] = tmp
                i = 2*i+2
            else:
                break
        return min_val
    def print_heap(self):
        self.print_heap_node(0,0)
    def print_heap_node(self, index, level):
        if index > len(self.arr) -1:
            return
        self.print_heap_node(index*2 + 2, level + 1)
        print(level*"\t" + str(self.arr[index]))
        self.print_heap_node(index*2 + 1, level + 1)