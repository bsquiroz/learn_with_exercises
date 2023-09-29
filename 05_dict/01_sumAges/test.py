import main as func
import data as info

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.sumAges(info.data1)
        self.assertEqual(res, 96)

    def test_2(self):
        res = func.sumAges(info.data2)
        self.assertEqual(res, 135)

    def test_3(self):
        res = func.sumAges(info.data3)
        self.assertEqual(res, 101)