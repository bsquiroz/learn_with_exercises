import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.evenNumber(5)
        self.assertEqual(res, 'es impar')

    def test_2(self):
        res = func.evenNumber(2)
        self.assertEqual(res, 'es par')

    def test_3(self):
        res = func.evenNumber(542)
        self.assertEqual(res, 'es par')

    def test_4(self):
        res = func.evenNumber(201)
        self.assertEqual(res, 'es impar')

    def test_5(self):
        res = func.evenNumber(110)
        self.assertEqual(res, 'es par')