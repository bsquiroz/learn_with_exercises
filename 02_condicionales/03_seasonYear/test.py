import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.seasonYear('febrero')
        self.assertEqual(res, 'Estamos en invierno')

    def test_2(self):
        res = func.seasonYear('mayo')
        self.assertEqual(res, 'Estamos en primavera')

    def test_3(self):
        res = func.seasonYear('agosto')
        self.assertEqual(res, 'Estamos en verano')

    def test_4(self):
        res = func.seasonYear('noviembre')
        self.assertEqual(res, 'Estamos en otoño')

    def test_5(self):
        res = func.seasonYear('narnia')
        self.assertEqual(res, 'Mes no válido')