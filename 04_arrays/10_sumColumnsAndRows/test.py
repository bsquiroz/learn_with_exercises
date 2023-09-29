import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.sumColumnsAndRows([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        self.assertEqual(res, [[6, 15, 24], [12, 15, 18]])

    def test_2(self):
        res = func.sumColumnsAndRows([
            [10, 2, 3],
            [4, 50, 6],
            [7, 8, 90]
        ])
        self.assertEqual(res, [[15, 60, 105], [21, 60, 99]])

    def test_3(self):
        res = func.sumColumnsAndRows([
            [1, 2, 30],
            [4, 50, 6],
            [70, 8, 9]
        ])
        self.assertEqual(res, [[33, 60, 87], [75, 60, 45]])
