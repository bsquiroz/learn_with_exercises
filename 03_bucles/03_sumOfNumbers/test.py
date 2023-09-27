import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.sumOfNumbers([1,2,3])
        self.assertEqual(res, 6)

    def test_2(self):
        res = func.sumOfNumbers([4,4,4])
        self.assertEqual(res, 12)

    def test_3(self):
        res = func.sumOfNumbers([10, 11, 29])
        self.assertEqual(res, 50)