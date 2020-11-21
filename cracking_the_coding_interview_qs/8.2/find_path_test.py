from find_path import find_path
import unittest

class Test_Case_Find_Path(unittest.TestCase):
    def test_find_path(self):
        grid = [
                [0,1,0,1],
                [0,0,1,0],
                [1,0,0,0],
                [1,0,0,0],
               ]
        ans = find_path(grid)
        print(ans)