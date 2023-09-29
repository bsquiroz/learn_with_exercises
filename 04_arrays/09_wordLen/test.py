import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.listWordLen('Esta sera una gran historia')
        self.assertEqual(res, [['Esta', 4], ['sera', 4], ['una', 3], ['gran', 4], ['historia', 8]])

    def test_2(self):
        res = func.listWordLen('Hola mundo desde RIWI')
        self.assertEqual(res, [['Hola', 4], ['mundo', 5], ['desde', 5], ['RIWI', 4]])

    def test_3(self):
        res = func.listWordLen('Esto apenas comienza, esto no para')
        self.assertEqual(res, [['Esto', 4], ['apenas', 6], ['comienza,', 9], ['esto', 4], ['no', 2], ['para', 4]])