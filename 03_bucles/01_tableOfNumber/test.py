import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.tableOfNumber(8)
        self.assertEqual(res, '8-16-24-32-40-48-56-64-72-80')

    def test_2(self):
        res = func.tableOfNumber(15)
        self.assertEqual(res,'15-30-45-60-75-90-105-120-135-150')

    def test_3(self):
        res = func.tableOfNumber(5)
        self.assertEqual(res,'5-10-15-20-25-30-35-40-45-50')