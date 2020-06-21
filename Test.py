import unittest

from Calculator import Calculator

class testCalculator(unittest.TestCase):
    def test_calc_pervtest(self):
        pervtest = Calculator(1,1,'+')
        rc = pervtest.calc()
        self.assertEqual(2,rc)

    def test_calc_vtortest(self):
        vtortest = Calculator(1)
        rc = vtortest.calc()
        self.assertEqual(1,rc)

    def test_calc_tretiytest(self):
        tretiytest = Calculator(h)
        rc = ptretiytest.calc()
        self.assertEqual(0, rc)

    def test_calc_chetvertyitest(self):
        chetvertyitest = Calculator('')
        rc = chetvertyitest.calc()
        self.assertEqual(0,rc)



unittest.main()
