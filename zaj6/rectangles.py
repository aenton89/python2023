from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2): # lewy dolny i prawy gorny
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(self.pt1, self.pt2)

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):        # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

    def area(self):                 # pole powierzchni
        return (abs(self.pt2.x - self.pt1.x)) * (abs(self.pt2.y - self.pt1.y))

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 
    def setUp(self):
        self.rectangle = Rectangle(0, 0, 2, 3)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "[(0, 0), (2, 3)]")

    def test_repr(self):
        self.assertEqual(repr(self.rectangle), "Rectangle(0, 0, 2, 3)")

    def test_eq(self):
        self.assertEqual(self.rectangle, Rectangle(0, 0, 2, 3))
        self.assertNotEqual(self.rectangle, Rectangle(1, 1, 3, 4))

    def test_ne(self):
        self.assertEqual(self.rectangle, Rectangle(0, 0, 2, 3))
        self.assertNotEqual(self.rectangle, Rectangle(1, 1, 3, 4))

    def test_center(self):
        self.assertEqual(self.rectangle.center(), Point(1, 1.5))

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 6)

    def test_move(self):
        self.rectangle.move(1, 1)
        self.assertEqual(self.rectangle, Rectangle(1, 1, 3, 4))

if __name__ == '__main__':
    unittest.main()    