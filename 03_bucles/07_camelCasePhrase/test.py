import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.camelCasePhrase('Hola mundo')
        self.assertEqual(res, 'holaMundo')

    def test_2(self):
        res = func.camelCasePhrase('Hola mundo desde RIWI')
        self.assertEqual(res, 'holaMundoDesdeRiwi')

    def test_3(self):
        res = func.camelCasePhrase('Sera que si esta duro')
        self.assertEqual(res, 'seraQueSiEstaDuro')