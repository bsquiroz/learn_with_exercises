import main as func

import unittest

class Prueba6(unittest.TestCase):
    def test_1(self):
        res = func.unionPhrase('Hola mundo')
        self.assertEqual(res, 'Holamundo')

    def test_2(self):
        res = func.unionPhrase('Este año aprendere a programar')
        self.assertEqual(res, 'Esteañoaprendereaprogramar')

    def test_3(self):
        res = func.unionPhrase('Hola, mi nombre es Riwi')
        self.assertEqual(res, 'Hola,minombreesRiwi')

