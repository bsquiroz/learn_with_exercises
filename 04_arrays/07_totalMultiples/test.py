import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.totalMultiples(3,5)
        self.assertEqual(res, [6, 9, 12, 15, 18])

    def test_2(self):
        res = func.totalMultiples(100, 3)
        self.assertEqual(res, [200, 300, 400])

    def test_3(self):
        res = func.totalMultiples(67, 5)
        self.assertEqual(res, [134, 201, 268, 335, 402])