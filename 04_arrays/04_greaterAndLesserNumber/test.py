import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.greaterAndLesserNumber([3,5,7,1,10])
        self.assertEqual(res, [1,10])

    def test_2(self):
        res = func.greaterAndLesserNumber([100, 150, 45, 23])
        self.assertEqual(res, [23, 150])

    def test_3(self):
        res = func.greaterAndLesserNumber([67, 8, 100, 888, 234])
        self.assertEqual(res, [8, 888])