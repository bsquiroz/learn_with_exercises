import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.repeatWord('Hola mundo')
        self.assertEqual(res, 'Hola-Hola-mundo-mundo')

    def test_2(self):
        res = func.repeatWord('Hola mundo desde RIWI')
        self.assertEqual(res, 'Hola-Hola-mundo-mundo-desde-desde-RIWI-RIWI')

    def test_3(self):
        res = func.repeatWord('Sera que si esta duro')
        self.assertEqual(res, 'Sera-Sera-que-que-si-si-esta-esta-duro-duro')