import heapq

class Get_Continous_Median():
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def get_median(self):
        if len(self.max_heap) != len(self.min_heap):
            return -1*self.max_heap[0]
        else:
            return (-1*self.max_heap[0] + self.min_heap[0]) / 2
    
    def add_num(self, num):
        if not self.max_heap:
            heapq.heappush(self.max_heap, -1*num)
            return
        m = self.get_median()
        if len(self.max_heap) == len(self.min_heap):
            if m > num:
                heapq.heappush(self.max_heap, -1*num)
            else:
                heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
        else:
            if m > num:
                heapq.heappush(self.min_heap, heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -1*num)
            else:
                heapq.heappush(self.min_heap, num)

