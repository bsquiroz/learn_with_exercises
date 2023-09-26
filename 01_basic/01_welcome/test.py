import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.welcome('Brayan')
        self.assertEqual(res, 'Hola a todos, mi nombre es Brayan')

    def test_2(self):
        res = func.welcome('Stiven')
        self.assertEqual(res, 'Hola a todos, mi nombre es Stiven')

    def test_3(self):
        res = func.welcome('Riwi')
        self.assertEqual(res, 'Hola a todos, mi nombre es Riwi')