import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.sortedByLen(['juan', 'pedro', 'brayan', 'alex', 'ana'])
        self.assertEqual(res, [['ana', 'juan', 'alex', 'pedro', 'brayan'], ['brayan', 'pedro', 'juan', 'alex', 'ana']])

    def test_2(self):
        res = func.sortedByLen(['alexander', 'pedronel', 'maurico', 'alex', 'ana'])
        self.assertEqual(res, [['ana', 'alex', 'maurico', 'pedronel', 'alexander'], ['alexander', 'pedronel', 'maurico', 'alex', 'ana']])

    def test_3(self):
        res = func.sortedByLen(['karen', 'carlos', 'maurico', 'agustous', 'ana'])
        self.assertEqual(res, [['ana', 'karen', 'carlos', 'maurico', 'agustous'], ['agustous', 'maurico', 'carlos', 'karen', 'ana']])