import unittest
from newttt import win

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


if __name__ == "__main__":
    unittest.main()
