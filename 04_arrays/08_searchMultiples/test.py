import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.searchMultiples(4,8)
        self.assertEqual(res, [4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_2(self):
        res = func.searchMultiples(3,10)
        self.assertEqual(res, [6, 12, 18, 24, 30])

    def test_3(self):
        res = func.searchMultiples(7,7)
        self.assertEqual(res, [14, 28, 42, 56])