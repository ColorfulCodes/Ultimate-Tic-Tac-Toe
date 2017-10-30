import unittest
from newttt import win
from newttt import check_full_x
from newttt import test_win


class TTTTests(unittest.TestCase):
    def test_win_x(self):
        board = ['X']*11
        expected = True
        actual = win(board, 'X')

        self.assertEquals(expected, actual)

    def test_not_win_x(self):
        board = ['O']*11
        expected = False
        actual = win(board, 'X')

        self.assertEquals(expected, actual)

    def test_check_full_x(self):
        board = ['X'] * 9
        expected = False
        actual = check_full_x(board,2)

        self.assertEquals(expected, actual)

    def test_not_check_full_x(self):
        board = [''] * 9
        #Failed
        expected = True
        actual = check_full_x(board,2)

        self.assertEquals(expected, actual)

    def test_test_win(self):
        board = ['X'] * 9
        expected = True
        actual = test_win(board,"X", 3)

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
