import unittest
from paint_fill import paint_fill

class Test_Case_Paint_Fill(unittest.TestCase):
    def test_paint_fill(self):
        arr = [
            ['b', 'b', 'w', 'b', 'b'],
            ['b', 'b', 'w', 'b', 'b'],
            ['b', 'b', 'w', 'w', 'b'],
            ['b', 'w', 'w', 'b', 'b'],
        ]
        paint_fill(arr, (0, 2), 'g')
        self.assertListEqual(arr,
        [
            ['b', 'b', 'g', 'b', 'b'],
            ['b', 'b', 'g', 'b', 'b'],
            ['b', 'b', 'g', 'g', 'b'],
            ['b', 'g', 'g', 'b', 'b'],
        ])