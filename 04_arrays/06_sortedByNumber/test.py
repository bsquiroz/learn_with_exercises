import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.sortedByNumber([1,5,2,9,3])
        self.assertEqual(res, [[1, 2, 3, 5, 9], [9, 5, 3, 2, 1]])

    def test_2(self):
        res = func.sortedByNumber([9,1,8,2])
        self.assertEqual(res, [[1, 2, 8, 9], [9, 8, 2, 1]])

    def test_3(self):
        res = func.sortedByNumber([99, 104,1,1002,3])
        self.assertEqual(res, [[1, 3, 99, 104, 1002], [1002, 104, 99, 3, 1]])