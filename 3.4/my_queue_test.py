import unittest
from my_queue import My_Queue

class Test_Case_My_Queue(unittest.TestCase):
    def test_my_queue(self):
        q = My_Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 2)