import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.sumTables(8)
        self.assertEqual(res, 440)

    def test_2(self):
        res = func.sumTables(15)
        self.assertEqual(res, 825)

    def test_3(self):
        res = func.sumTables(5)
        self.assertEqual(res, 275)