import main as func

import unittest

class Prueba8(unittest.TestCase):
    def test_1(self):
        res = func.lenEndWord('Hola mundo desde riwi')
        self.assertEqual(res, 4)

    def test_2(self):
        res = func.lenEndWord('Esto es de lo mejor')
        self.assertEqual(res, 5)

    def test_3(self):
        res = func.lenEndWord('Aprendiendo fundamentos en python')
        self.assertEqual(res, 6)
