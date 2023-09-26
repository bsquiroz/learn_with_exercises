import main as func

import unittest

class Prueba4(unittest.TestCase):
    def test_1(self):
        res = func.chartEnd('brayan')
        self.assertEqual(res, 'n')

    def test_2(self):
        res = func.chartEnd('Hello world')
        self.assertEqual(res, 'd')

    def test_3(self):
        res = func.chartEnd('Hola RIWI')
        self.assertEqual(res, 'I')

