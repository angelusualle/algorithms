import unittest
from check_tic_tac_toe_board import check_win

class Test_Case_Check_Tic_Tac_Toe_Board(unittest.TestCase):
    def test_check_tic_tac_toe_board(self):
        board = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['o', 'o', 'x']
        ]
        self.assertTrue(check_win(board))
        board = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['o', 'x', 'o']
        ]
        self.assertFalse(check_win(board))