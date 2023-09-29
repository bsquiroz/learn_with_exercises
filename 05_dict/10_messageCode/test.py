import main as func
import data as info

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.messageCode(info.my_dict, info.data1)
        self.assertEqual(res, info.res1)

    def test_2(self):
        res = func.messageCode(info.my_dict, info.data2)
        self.assertEqual(res, info.res2)

    def test_3(self):
        res = func.messageCode(info.my_dict, info.data3)
        self.assertEqual(res, info.res3)

    def test_4(self):
        res = func.messageCode(info.my_dict, info.data4)
        self.assertEqual(res, info.res4)