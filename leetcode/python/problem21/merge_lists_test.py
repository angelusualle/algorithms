import unittest
from merge_lists import merge_lists, ListNode

class Test_Case_Merge_Lists(unittest.TestCase):
    def test_merge_lists(self):
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        merged = merge_lists(l1, l2)
        answer = []
        next_ = merged
        while next_ is not None:
            answer.append(next_.val)
            next_ = next_.next
        self.assertListEqual(answer, [1,1,2,3,4,4])

if __name__ == '__main__':
    unittest.main()
