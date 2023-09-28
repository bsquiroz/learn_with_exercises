import main as func

import unittest

class Prueba2(unittest.TestCase):
    def test_1(self):
        res = func.unionSimbols('Hola mundo me llamo RIWI', '*')
        self.assertEqual(res, 'Hola*mundo*me*llamo*RIWI')

    def test_2(self):
        res = func.unionSimbols('Este ejercicio está muy fácil', '-')
        self.assertEqual(res, 'Este-ejercicio-está-muy-fácil')

    def test_3(self):
        res = func.unionSimbols('Aquí sí aprenderé a trabajar', '+')
        self.assertEqual(res, 'Aquí+sí+aprenderé+a+trabajar')
