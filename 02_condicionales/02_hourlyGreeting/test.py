import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.hourlyGreeting(2)
        self.assertEqual(res, 'Deberías estar durmiendo')

    def test_2(self):
        res = func.hourlyGreeting(7)
        self.assertEqual(res, 'Buenos días')

    def test_3(self):
        res = func.hourlyGreeting(13)
        self.assertEqual(res, 'Buenas tardes')

    def test_4(self):
        res = func.hourlyGreeting(20)
        self.assertEqual(res, 'Buenas noches')

    def test_5(self):
        res = func.hourlyGreeting(25)
        self.assertEqual(res, 'Hora no soportada')