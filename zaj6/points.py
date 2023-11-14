import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):        # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 
    def test_str(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1, 2)")

    def test_repr(self):
        p = Point(1, 2)
        self.assertEqual(repr(p), "Point(1, 2)")

    def test_eq(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(2, 3)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_add(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 + p2, Point(4, 6))

    def test_sub(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 - p2, Point(-2, -2))

    def test_mul(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1 * p2, 11)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        self.assertEqual(p1.cross(p2), -2)

    def test_length(self):
        p = Point(3, 4)
        self.assertEqual(p.length(), 5)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy