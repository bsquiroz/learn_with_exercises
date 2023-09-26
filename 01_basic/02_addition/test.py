import main as func

import unittest

class Prueba2(unittest.TestCase):
    def test_1(self):
        res = func.addition(1, 4)
        self.assertEqual(res, 5)

    def test_2(self):
        res = func.addition(5, 4)
        self.assertEqual(res, 9)

    def test_3(self):
        res = func.addition(3, 5)
        self.assertEqual(res, 8)
