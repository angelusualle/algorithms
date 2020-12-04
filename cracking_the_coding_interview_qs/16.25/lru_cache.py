# O(1) inserts, retrievals, employing LRU cache eviction policy
class LRU_Cache():
    class LinkedListNode():
        def __init__(self):
            self.val = None
            self.key = None
            self.next = None
            self.prev = None
    
    def __init__(self, max_size=50):
        self.max_size = max_size
        self.size = 0
        self.head = None
        self.end = None
        self.key_to_linked_list = {}

    def add_item(self, key, value):
        node = LRU_Cache.LinkedListNode()
        node.val = value
        node.key = key
        if self.head is None:
            self.head = node
            self.end = node
            self.size += 1
        else:
            if self.size == self.max_size:
                self.evict_oldest()
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.size += 1
        self.key_to_linked_list[key] = node
    
    def evict_oldest(self):
        key = self.end.key
        del self.key_to_linked_list[key]
        self.end = self.end.prev
        self.end.next = None
        self.size -= 1
    
    def get_item(self, key):
        if key not in self.key_to_linked_list:
            return None
        node = self.key_to_linked_list[key]
        self.move_node_to_top(node)
        return node.val
    
    def move_node_to_top(self, node):
        if node == self.head:
            return
        if node == self.end:
            self.end = self.end.prev
            self.end.next = None
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
    
