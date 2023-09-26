import main as func

import unittest

class Prueba10(unittest.TestCase):
    def test_1(self):
        res = func.upperEndWord('Hola mundo desde riwi')
        self.assertEqual(res, 'RIWI')

    def test_2(self):
        res = func.upperEndWord('Esto es de lo mejor')
        self.assertEqual(res, 'MEJOR')

    def test_3(self):
        res = func.upperEndWord('Aprendiendo fundamentos en python')
        self.assertEqual(res, 'PYTHON')