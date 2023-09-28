import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.amountVocals('Esta sera una gran historia')
        self.assertEqual(res, 11)

    def test_2(self):
        res = func.amountVocals('Hola mundo desde RIWI')
        self.assertEqual(res, 8)

    def test_3(self):
        res = func.amountVocals('Esto apenas comienza, esto no para')
        self.assertEqual(res, 14)