import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.twoWords('Hola mundo')
        self.assertEqual(res, 'Hlmno y oaud')

    def test_2(self):
        res = func.twoWords('Hola mundo desde RIWI')
        self.assertEqual(res, 'HlmnoedRW y oauddseII')

    def test_3(self):
        res = func.twoWords('Sera que si esta duro')
        self.assertEqual(res, 'Srqeisauo y eausetdr')