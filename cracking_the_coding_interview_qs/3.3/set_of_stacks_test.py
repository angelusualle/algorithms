import unittest
from set_of_stacks import Set_Of_Stacks

class Test_Case_Set_Of_Stacks(unittest.TestCase):
    def test_set_of_stacks(self):
        set_stacks = Set_Of_Stacks(2)
        set_stacks.push(1)
        set_stacks.push(2)
        set_stacks.push(3)
        set_stacks.push(4)
        set_stacks.push(5)
        self.assertEqual(set_stacks.pop(), 5)
        self.assertEqual(set_stacks.pop(), 4)
        self.assertEqual(set_stacks.pop_at(1), 3)