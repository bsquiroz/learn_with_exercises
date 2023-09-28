import main as func

import unittest

class Prueba1(unittest.TestCase):
    def test_1(self):
        res = func.amountVocals('Esta sera una gran historia')
        self.assertEqual(res, 'e__a _e_a u_a __a_ _i__o_ia')

    def test_2(self):
        res = func.amountVocals('Hola mundo desde RIWI')
        self.assertEqual(res, '_o_a _u__o _e__e _i_i')

    def test_3(self):
        res = func.amountVocals('Esto apenas comienza, esto no para')
        self.assertEqual(res, 'e__o a_e_a_ _o_ie__a_ e__o _o _a_a')