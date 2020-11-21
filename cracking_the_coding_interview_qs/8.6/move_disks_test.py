import unittest
from move_disks import move_disks

class Test_Case_Move_Disks(unittest.TestCase):
    def test_move_disks(self):
        start = [5,4,3,2,1]
        buffer = []
        end = []
        move_disks(len(start), start, buffer, end)
        self.assertListEqual([5,4,3,2,1], end)