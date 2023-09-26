import main as func

import unittest

class Prueba9(unittest.TestCase):
    def test_1(self):
        res = func.wordInPhrase('Hola mundo desde riwi', 'mundo')
        self.assertEqual(res, True)

    def test_2(self):
        res = func.wordInPhrase('Esto es de lo mejor', 'Mejor')
        self.assertEqual(res, False)

    def test_3(self):
        res = func.wordInPhrase('Aprendiendo fundamentos en python', 'python')
        self.assertEqual(res, True)