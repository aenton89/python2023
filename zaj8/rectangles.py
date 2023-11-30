from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if (isinstance(x1, int | float) and isinstance(x2, int | float) and isinstance(y1, int | float) and isinstance(y2, int | float)):
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError("niepoprawna wartosc punktow")

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(self.pt1, self.pt2)

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):        # obsługa rect1 == rect2
        if(isinstance(other, Rectangle)):
            return self.pt1 == other.pt1 and self.pt2 == other.pt2
        else:
            raise ValueError("other nie jest prostokatem")

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt2.y)
    
    @property
    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):                 # pole powierzchni
        return self.width * self.height

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

    def intersection(self, other):  # część wspólna prostokątów
        if(isinstance(other, Rectangle)):
            x1 = max(self.pt1.x, other.pt1.x)
            y1 = max(self.pt1.y, other.pt1.y)
            x2 = min(self.pt2.x, other.pt2.x)
            y2 = min(self.pt2.y, other.pt2.y)
            if(x1 < x2 and y1 < y2):
                return Rectangle(x1, y1, x2, y2)
            else:
                raise ValueError("prostokaty nie maja czesci wspolnej")
        else:
            raise ValueError("other nie jest prostokatem")
            
    def cover(self, other):         # prostąkąt nakrywający oba
        if(isinstance(other, Rectangle)):
            return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        else:
            raise ValueError("other nie jest prostokatem")

    def make4(self):                # zwraca krotkę czterech mniejszych
        x1 = self.pt1.x
        y1 = self.pt1.y
        x2 = self.pt2.x
        y2 = self.pt2.y
        x3 = (x1 + x2) / 2
        y3 = (y1 + y2) / 2
        return (Rectangle(x1, y1, x3, y3), Rectangle(x3, y1, x2, y3), Rectangle(x1, y3, x3, y2), Rectangle(x3, y3, x2, y2))
    # A-------B   po podziale  A---+---B
    # |       |                |   |   |
    # |       |                +---+---+
    # |       |                |   |   |
    # D-------C                D---+---C

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("niepoprawna liczba punktow")
        p1 = points[0]
        p2 = points[1]
        return cls(p1.x, p1.y, p2.x, p2.y)