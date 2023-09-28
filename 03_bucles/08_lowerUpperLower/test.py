import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.lowerUpperLower('Esta sera una gran historia')
        self.assertEqual(res, 'eStA SeRa uNa gRaN HiStOrIa')

    def test_2(self):
        res = func.lowerUpperLower('Hola mundo desde RIWI')
        self.assertEqual(res, 'hOlA MuNdO DeSdE RiWi')

    def test_3(self):
        res = func.lowerUpperLower('Esto apenas comienza, esto no para')
        self.assertEqual(res, 'eStO ApEnAs cOmIeNzA, eStO No pArA')