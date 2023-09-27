import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.dobleNumberOrNumber(10)
        self.assertEqual(res, 20)

    def test_2(self):
        res = func.dobleNumberOrNumber(20)
        self.assertEqual(res, 20)

    def test_3(self):
        res = func.dobleNumberOrNumber(5)
        self.assertEqual(res, 10)

    def test_4(self):
        res = func.dobleNumberOrNumber(8)
        self.assertEqual(res, 16)

    def test_5(self):
        res = func.dobleNumberOrNumber(11)
        self.assertEqual(res, 11)