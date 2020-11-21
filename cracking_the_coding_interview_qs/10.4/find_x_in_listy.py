class Listy():
    def __init__(self, arr):
        self.arr = arr
    def element_at(self, pos):
        return -1 if pos > (len(self.arr) - 1) else self.arr[pos]

def find_x_in_listy(listy, val):
    i = 0
    if listy.element_at(1) == -1:
        return 0 if listy.element_at(0) == val else None
    while listy.element_at(int(2 ** i)) != -1:
        i += 1
    low= int(2**(i-1))
    high = int(2 ** i)
    last_idx = -1
    while low <= high:
        mid = (high + low) // 2
        if listy.element_at(mid) != -1:
            last_idx = max(last_idx, mid)
            low = mid + 1
        else:
            high = mid - 1
    low = 0
    high = last_idx
    while low <= high:
        mid = (high + low) // 2
        if listy.element_at(mid) == val:
            return mid
        elif listy.element_at(mid) < val:
            low = mid + 1
        else:
            high = mid - 1
    return None

