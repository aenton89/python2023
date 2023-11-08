import math

def add_frac(frac1, frac2):             # frac1 + frac2
    gcd =  math.gcd(frac1[1], frac2[1])
    numerator1 = int(frac1[0] * (frac2[1] / gcd))
    numerator2 = int(frac2[0] * (frac1[1] / gcd))
    denominator = int((frac1[1] * frac2[1]) / gcd)
    secondGcd = math.gcd(numerator1 + numerator2, denominator)

    if (secondGcd != 1):
        return [(numerator1 + numerator2) / secondGcd, denominator / secondGcd]
    else:
        return [numerator1 + numerator2, denominator]

def sub_frac(frac1, frac2):             # frac1 - frac2
    gcd =  math.gcd(frac1[1], frac2[1])
    numerator1 = int(frac1[0] * (frac2[1] / gcd))
    numerator2 = int(frac2[0] * (frac1[1] / gcd))
    denominator = int((frac1[1] * frac2[1]) / gcd)
    secondGcd = math.gcd(numerator1 - numerator2, denominator)

    if (secondGcd != 1):
        return [(numerator1 - numerator2) / secondGcd, denominator / secondGcd]
    else:
        return [numerator1 - numerator2, denominator]

def mul_frac(frac1, frac2):             # frac1 * frac2
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(numerator, denominator)
    return [numerator / gcd, denominator / gcd]

def div_frac(frac1, frac2):             # frac1 / frac2
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    gcd = math.gcd(numerator, denominator)
    return [numerator / gcd, denominator / gcd]

def is_positive(frac):                  # bool, czy dodatni
    return frac[0] * frac[1] > 0

def is_zero(frac):                      # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2):             # -1 | 0 | +1
    gcd = math.gcd(frac1[1], frac2[1])
    numerator1 = frac1[0] * (frac2[1])
    numerator2 = frac2[0] * (frac1[1])
    
    if numerator1 < numerator2:
        return -1
    elif numerator1 == numerator2:
        return 0
    else:
        return 1

def frac2float(frac):                   # konwersja do float
    return (frac[0] / frac[1])

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 14], [3, 21]), [2, 7])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([2, 14], [3, 21]), [0, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([2, 14], [3, 21]), [1, 49])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([2, 14], [3, 21]), [1, 1])

    def test_is_positive(self): 
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertTrue(is_positive([-1, -2]))

    def test_is_zero(self): 
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self): 
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 2], [3, 4]), -1)

    def test_frac2float(self): 
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([-1, 3]), -1/3)
        self.assertEqual(frac2float([0, 2]), 0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy