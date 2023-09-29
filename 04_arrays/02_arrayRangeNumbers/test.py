import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.arrayRangeNumbers(11, 17)
        self.assertEqual(res, [11,12,13,14,15,16,17])

    def test_2(self):
        res = func.arrayRangeNumbers(6, 10)
        self.assertEqual(res, [6,7,8,9,10])

    def test_3(self):
        res = func.arrayRangeNumbers(3,9)
        self.assertEqual(res, [3,4,5,6,7,8,9])