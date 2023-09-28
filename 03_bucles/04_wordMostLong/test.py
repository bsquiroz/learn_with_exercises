import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.wordMostLong('Esta sera una gran historia')
        self.assertEqual(res, 'historia')

    def test_2(self):
        res = func.wordMostLong('Hola mundo desde RIWI')
        self.assertEqual(res, 'desde')

    def test_3(self):
        res = func.wordMostLong('Esto de verdad que apenas comienza')
        self.assertEqual(res, 'comienza')