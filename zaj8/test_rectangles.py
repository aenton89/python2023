import pytest
from rectangles import Rectangle
from points import Point

def test_rectangle_init():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 3
    assert rect.top == 4

def test_rectangle_str():
    rect = Rectangle(1, 2, 3, 4)
    assert str(rect) == "[(1, 2), (3, 4)]"

def test_rectangle_repr():
    rect = Rectangle(1, 2, 3, 4)
    assert repr(rect) == "Rectangle(1, 2, 3, 4)"

def test_rectangle_eq():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(1, 2, 3, 4)
    assert rect1 == rect2

def test_rectangle_ne():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(5, 6, 7, 8)
    assert rect1 != rect2

def test_rectangle_center():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.center == Point(2, 3)

def test_rectangle_area():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.area() == 4

def test_rectangle_move():
    rect = Rectangle(1, 2, 3, 4)
    rect.move(1, 1)
    assert rect.left == 2
    assert rect.bottom == 3
    assert rect.right == 4
    assert rect.top == 5

def test_rectangle_intersection():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(2, 3, 4, 5)
    intersection = rect1.intersection(rect2)
    assert intersection.left == 2
    assert intersection.bottom == 3
    assert intersection.right == 3
    assert intersection.top == 4

def test_rectangle_cover():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(2, 3, 4, 5)
    cover = rect1.cover(rect2)
    assert cover.left == 1
    assert cover.bottom == 2
    assert cover.right == 4
    assert cover.top == 5

def test_rectangle_make4():
    rect = Rectangle(1, 2, 3, 4)
    rects = rect.make4()
    assert rects[0].left == 1
    assert rects[0].bottom == 2
    assert rects[0].right == 2
    assert rects[0].top == 3
    assert rects[1].left == 2
    assert rects[1].bottom == 2
    assert rects[1].right == 3
    assert rects[1].top == 3
    assert rects[2].left == 1
    assert rects[2].bottom == 3
    assert rects[2].right == 2
    assert rects[2].top == 4
    assert rects[3].left == 2
    assert rects[3].bottom == 3
    assert rects[3].right == 3
    assert rects[3].top == 4

def test_rectangle_from_points():
    points = [Point(1, 2), Point(3, 8)]
    rect = Rectangle.from_points(points)
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 3
    assert rect.top == 8