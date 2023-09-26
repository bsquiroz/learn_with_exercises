import main as func

import unittest

class Prueba5(unittest.TestCase):
    def test_1(self):
        res = func.wordEnd('Hola mundo')
        self.assertEqual(res, 'mundo')

    def test_2(self):
        res = func.wordEnd('Este año aprendere a programar')
        self.assertEqual(res, 'programar')

    def test_3(self):
        res = func.wordEnd('Hola, mi nombre es Riwi')
        self.assertEqual(res, 'Riwi')
