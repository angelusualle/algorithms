import unittest
from merge_k_lists import merge_k_lists, ListNode

class Test_Case_Merge_K_Lists(unittest.TestCase):
    def test_merge_k_lists(self):
        lists = [ListNode(1, ListNode(2, ListNode(2))), ListNode(1, ListNode(1, ListNode(2)))]
        answer = merge_k_lists(lists)
        answer_collector = []
        while answer is not None:
            answer_collector.append(answer.val)
            answer = answer.next
        self.assertListEqual(answer_collector, [1,1, 1, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()
