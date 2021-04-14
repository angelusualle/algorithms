import unittest
from swap_pairs import swap_pairs, ListNode

class Test_Case_Swap_Pairs(unittest.TestCase):
    def test_swap_pairs(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        next_ = swap_pairs(head)
        ans = []
        while next_ is not None:
            ans.append(next_.val)
            next_ = next_.next
        self.assertListEqual(ans, [2,1,4,3])

if __name__ == '__main__':
    unittest.main()