import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.ricePaisa('pequeña')
        self.assertEqual(res, 'Caja de arroz pequeña: $10')

    def test_2(self):
        res = func.ricePaisa('mediana')
        self.assertEqual(res, 'Caja de arroz mediana: $15')

    def test_3(self):
        res = func.ricePaisa('grande')
        self.assertEqual(res, 'Caja de arroz grande: $20')

    def test_4(self):
        res = func.ricePaisa('familiar')
        self.assertEqual(res, 'Caja de arroz familiar: $25')

    def test_4(self):
        res = func.ricePaisa('perro')
        self.assertEqual(res, 'No está disponible')