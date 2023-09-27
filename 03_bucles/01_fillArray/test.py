import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.fillArray(7)
        self.assertEqual(res, [1,2,3,4,5,6,7])

    def test_2(self):
        res = func.fillArray(3)
        self.assertEqual(res, [1,2,3])

    def test_3(self):
        res = func.fillArray(11)
        self.assertEqual(res, [1,2,3,4,5,6,7,8,9,10,11])