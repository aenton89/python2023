import math

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError("mianownik nie moze byc 0")
        gcd = math.gcd(int(x), int(y))
        x = x / gcd
        y = y / gcd
        self.x = int(x)
        self.y = int(y)

    def __str__(self):              # zwraca "x/y" lub "x" dla y=1
        return "{0}/{1}".format(self.x, self.y) if self.y != 1 else str(self.x)

    def __repr__(self):             # zwraca "Frac(x, y)"
        return "Frac({0}, {1})".format(self.x, self.y)

    # Py2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, int)):
                other = Frac(other)
            elif(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            gcd = math.gcd(int(self.y), int(other.y))
            numerator1 = self.x * (other.y / gcd)
            numerator2 = other.x * (self.y / gcd)

            return numerator1 == numerator2
        else:
            raise ValueError("nie mozna porownac podanej wartosci")

    def __ne__(self, other): 
        return not self == other

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, int)):
                other = Frac(other) 
            elif(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            gcd = math.gcd(int(self.y), int(other.y))
            numerator1 = self.x * (other.y / gcd)
            numerator2 = other.x * (self.y / gcd)

            return numerator1 < numerator2
        else:
            raise ValueError("nie mozna porownac podanej wartosci")

    def __le__(self, other): 
        if isinstance(other, int) or isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, int)):
                other = Frac(other) 
            elif(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            gcd = math.gcd(int(self.y), int(other.y))
            numerator1 = self.x * (other.y / gcd)
            numerator2 = other.x * (self.y / gcd)

            return numerator1 <= numerator2
        else:
            raise ValueError("nie mozna porownac podanej wartosci")

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):       # frac1+frac2, frac+int
        if isinstance(other, int):
            return Frac(self.x + other*self.y, self.y)
        elif isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            gcd = math.gcd(int(self.y), int(other.y))
            numerator1 = self.x * (other.y / gcd)
            numerator2 = other.x * (self.y / gcd)
            denominator = (self.y * other.y) / gcd
            secondGcd = math.gcd(int(numerator1 + numerator2), int(denominator))

            if (secondGcd != 1):
                return Frac(int((numerator1 + numerator2) / secondGcd), int(denominator / secondGcd))
            else:
                return Frac(int(numerator1 + numerator2), int(denominator))
        else:
            raise ValueError("nie mozna dodac podanej wartosci")

    __radd__ = __add__              # int+frac

    def __sub__(self, other):       # frac1-frac2, frac-int
        if isinstance(other, int):
            return Frac(self.x - other*self.y, self.y)
        elif isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            gcd = math.gcd(int(self.y), int(other.y))
            numerator1 = self.x * (other.y / gcd)
            numerator2 = other.x * (self.y / gcd)
            denominator = (self.y * other.y) / gcd
            secondGcd = math.gcd(int(numerator1 - numerator2), int(denominator))

            if (secondGcd != 1):
                return Frac(int((numerator1 - numerator2) / secondGcd), int(denominator / secondGcd))
            else:
                return Frac(int(numerator1 - numerator2), int(denominator))
        else:
            raise ValueError("nie mozna odjac podanej wartosci")

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):       # frac1*frac2, frac*int
        if isinstance(other, int):
            gcd = math.gcd(int(self.y), int(other))
            r = other / gcd
            return Frac(int(self.x * r), int(self.y / gcd))
        elif isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            numerator = self.x * other.x
            denominator = self.y * other.y
            gcd = math.gcd(int(numerator), int(denominator))
            return Frac(int(numerator / gcd), int(denominator / gcd))
        else:
            raise ValueError("nie mozna mnozyc przez podana wartosc")

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):       # frac1/frac2, frac/int, Py2
        if isinstance(other, int):
            gcd = math.gcd(int(self.x), int(other))
            r = other / gcd
            return Frac(int(self.x / gcd), int(self.y * r))
        elif isinstance(other, Frac) or isinstance(other, float):
            if(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            numerator = self.x * other.y
            denominator = self.y * other.x
            gcd = math.gcd(int(numerator), int(denominator))
            return Frac(int(numerator / gcd), int(denominator / gcd))
        else:
            raise ValueError("nie mozna dzielic przez podana wartosc")

    def __rdiv__(self, other):      # int/frac, Py2
        if(isinstance(other, int)):
            gcd = math.gcd(int(self.y), int(other))
            r = other / gcd
            return Frac(int(self.y * r), int(self.x / gcd))
        elif(isinstance(other, float)):
            other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            gcd = math.gcd(int(self.y), int(other.x))
            r = other.x / gcd
            return Frac(int(self.y * r), int(self.x / gcd))
        else:
            raise ValueError("nie mozna dzielic przez podana wartosc")

    def __truediv__(self, other):   # frac1/frac2, frac/int, Py3
        if(isinstance(other, int)):
            return float(self.x / (self.y * other))
        elif(isinstance(other, Frac) or isinstance(other, float)):
            if(isinstance(other, float)):
                other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            return float(self.x * other.y / self.y * other.x)
        else:
            raise ValueError("nie mozna dzielic przez podana wartosc")
        
    def __rtruediv__(self, other):  # int/frac, Py3
        if(isinstance(other, int)):
            return float(self.y * other / self.x)
        elif(isinstance(other, float)):
            other = Frac(other.as_integer_ratio()[0], other.as_integer_ratio()[1])
            return float(self.y * other.x / self.x * other.y)
        else:
            raise ValueError("nie mozna dzielic przez podana wartosc")

    # operatory jednoargumentowe
    def __pos__(self):              # +frac = (+1)*frac
        return self

    def __neg__(self):              # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):           # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):            # float(frac)
        return float(self.x / self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])



# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase): 
    def test_init(self):
        frac = Frac(3, 4)
        self.assertEqual(frac.x, 3)
        self.assertEqual(frac.y, 4)

    def test_str(self):
        frac = Frac(3, 4)
        self.assertEqual(str(frac), "3/4")
        frac2 = Frac(5)
        self.assertEqual(str(frac2), "5")

    def test_repr(self):
        frac = Frac(3, 4)
        self.assertEqual(repr(frac), "Frac(3, 4)")

    def test_eq(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(6, 8)
        self.assertTrue(frac1 == frac2)
        self.assertTrue(frac1 == 0.75)

        frac3 = Frac(5)
        self.assertTrue(frac3 == 5)

        self.assertRaises(ValueError, frac1.__eq__, "abc")

    def test_ne(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(5, 6)
        self.assertTrue(frac1 != frac2)

    def test_lt(self):
        f1 = Frac(3, 4)
        f2 = Frac(5, 6)
        self.assertTrue(f1 < f2)
        self.assertTrue(f1 < 1)
        self.assertFalse(f1 < 0.5)

    def test_le(self):
        f1 = Frac(3, 4)
        f2 = Frac(5, 6)
        self.assertTrue(f1 <= f2)
        self.assertTrue(f1 <= 0.75)

    def test_add(self):
        f1 = Frac(3, 4)
        f2 = Frac(1, 2)
        result = f1 + f2
        self.assertEqual(result, Frac(5, 4))

        result = f1 + 2
        self.assertEqual(result, Frac(11, 4))

        result = f1 + 0.25
        self.assertEqual(result, Frac(1,1))

        self.assertRaises(ValueError, f1.__add__, "abc")

    def test_radd(self):
        f1 = Frac(3,4)
        result = 1 + f1
        self.assertEqual(result, Frac(7, 4))

    def test_sub(self):
        f1 = Frac(3, 4)
        f2 = Frac(1, 2)
        result = f1 - f2
        self.assertEqual(result, Frac(1, 4))

        result = f1 - 2
        self.assertEqual(result, Frac(-5, 4))

        result = f1 - 0.75
        self.assertEqual(result, Frac())

        self.assertRaises(ValueError, f1.__sub__, "abc")

    def test_rsub(self):
        f1 = Frac(3, 4)
        result = 2 - f1
        self.assertEqual(result, Frac(5, 4))

    def test_mul(self):
        f1 = Frac(3, 4)
        f2 = Frac(1, 2)
        result = f1 * f2
        self.assertEqual(result, Frac(3, 8))

        result = f1 * 2
        self.assertEqual(result, Frac(3, 2))

        result = f1 * 0.25
        self.assertEqual(result, Frac(3, 16))

        self.assertRaises(ValueError, f1.__mul__, "abc")

    def test_rmul(self):
        f1 = Frac(3,4)
        result = 2 * f1
        self.assertEqual(result, Frac(3, 2))

    def test_div(self):
        f1 = Frac(3, 4)
        f2 = Frac(1, 2)
        result = f1 / f2
        self.assertEqual(result, Frac(3, 2))

        result = f1 / 2
        self.assertEqual(result, Frac(3, 8))

        result = f1 / 0.25
        self.assertEqual(result, Frac(3))

        self.assertRaises(ValueError, f1.__div__, "abc")

    def test_rdiv(self):
        f1 = Frac(3, 4)
        result = 2 / f1
        self.assertEqual(result, Frac(8, 3))

    def test_truediv(self):
        f1 = Frac(3, 4)
        f2 = Frac(1, 2)
        result = f1.__truediv__(f2)
        self.assertEqual(result, 1.5)

        result = f1.__truediv__(2)
        self.assertEqual(result, 0.375)

        result = f1.__truediv__(0.25)
        self.assertEqual(result, 3.0)

        self.assertRaises(ValueError, f1.__truediv__, "abc")

    def test_rtruediv(self):
        f1 = Frac(4, 3)
        result = f1.__rtruediv__(2)
        self.assertEqual(result, 1.5)

    def test_pos(self):
        f = Frac(3, 4)
        self.assertEqual(+f, f)

    def test_neg(self):
        f = Frac(3, 4)
        self.assertEqual(-f, Frac(-3, 4))

    def test_invert(self):
        f = Frac(3, 4)
        self.assertEqual(~f, Frac(4, 3))

    def test_float(self):
        f = Frac(3, 4)
        self.assertEqual(float(f), 0.75)

    def test_hash(self):
        f1 = Frac(3, 4)
        f2 = Frac(6, 8)
        self.assertEqual(hash(f1), hash(f2))
    
    
    
    
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy