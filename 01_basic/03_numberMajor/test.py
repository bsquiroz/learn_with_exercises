import main as func

import unittest

class Prueba3(unittest.TestCase):
    def test_1(self):
        res = func.numberMajor(1, 4, 7)
        self.assertEqual(res, 7)

    def test_2(self):
        res = func.numberMajor(5, 8, 4)
        self.assertEqual(res, 8)

    def test_3(self):
        res = func.numberMajor(19, 3, 5)
        self.assertEqual(res, 19)
