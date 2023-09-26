import main as func

import unittest

class Prueba7(unittest.TestCase):
    def test_1(self):
        res = func.countCharacters('Hola mundo')
        self.assertEqual(res, 10)

    def test_2(self):
        res = func.countCharacters('Hola riwi')
        self.assertEqual(res, 9)

    def test_3(self):
        res = func.countCharacters('brayan')
        self.assertEqual(res, 6)

