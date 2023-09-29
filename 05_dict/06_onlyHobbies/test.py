import main as func
import data as info

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.onlyHobbies(info.data1)
        self.assertEqual(res, info.res1)

    def test_2(self):
        res = func.onlyHobbies(info.data2)
        self.assertEqual(res, info.res2)

    def test_3(self):
        res = func.onlyHobbies(info.data3)
        self.assertEqual(res, info.res3)