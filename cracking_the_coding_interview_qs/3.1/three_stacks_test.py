import unittest
from three_stacks import Three_Stacks

class Test_Case_Three_Stacks(unittest.TestCase):
    def test_three_stacks(self):
        stacks = Three_Stacks()
        stacks.push(0, 'first_push_0')
        stacks.push(0, 'second_push_0')
        stacks.push(1, 'first_push_1')
        self.assertEqual(stacks.pop(0), 'second_push_0')
        self.assertEqual(stacks.pop(1), 'first_push_1')

if __name__ == '__main__':
    unittest.main()