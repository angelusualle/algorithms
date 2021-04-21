import unittest
from reverse_k_group import ListNode, reverse_k_group

class Test_Case_Reverse_K_Group(unittest.TestCase):
    def test_reverse_k_group(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        next_ = reverse_k_group(head, 2)
        ans = []
        while next_ is not None:
            ans.append(next_.val)
            next_ = next_.next
        self.assertListEqual(ans, [2,1,4,3])