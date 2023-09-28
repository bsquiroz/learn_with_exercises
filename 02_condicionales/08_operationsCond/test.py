import main as func

import unittest

class Prueba3(unittest.TestCase):
    def test_1(self):
        res = func.firstOrEnd([1,2,3,4,5])
        self.assertEqual(res, 1)

    def test_2(self):
        res = func.firstOrEnd([1,2,3,4])
        self.assertEqual(res, 4)

    def test_3(self):
        res = func.firstOrEnd([32,43,21])
        self.assertEqual(res, 32)
    
    def test_4(self):
        res = func.firstOrEnd([1,2,3,4,5,54,65,76,1,95])
        self.assertEqual(res, 95)
