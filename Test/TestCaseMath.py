from unittest import TestCase
from myMath.math import Square, Rectangle, Triangle, Circle, Cone

class TestSquare(TestCase):
    def test_square_surface_area(self):
        sqr = Square()
        result = sqr.surface_area(2)
        self.assertEqual(result, 4)

    def test_square_circuit(self):
        sqr = Square()
        result = sqr.circuit(4)
        self.assertEqual(result, 16)


class TestRectangle(TestCase):
    def test_rectangle_surface_are(self):
        rec = Rectangle()
        result = rec.surface_area(2, 3)
        self.assertEqual(result, 6)

    def test_rectangle_circuit(self):
        rec = Rectangle()
        result = rec.circuit(4, 5)
        self.assertEqual(result, 18)


class TestTriangle(TestCase):
    def test_triangle_surface_are(self):
        tri = Triangle()
        result = tri.surface_area(2, 3)
        self.assertEqual(result, 3)

    def test_triangle_circuit(self):
        tri = Triangle()
        result = tri.circuit(1, 2, 3)
        self.assertEqual(result, 6)


class TestCircle(TestCase):
    def test_circle_surface_area(self):
        cir = Circle()
        result = cir.surface_area(2)
        self.assertEqual(result, 12.566370614359172)
    def test_circle_circuit(self):
        cir = Circle()
        result = cir.circuit(5)
        self.assertEqual(result, 31.41592653589793)


class TestCone(TestCase):
    def test_cone_surface_area(self):
        con = Cone()
        result = con.surface_area(3,4)
        self.assertEqual(result, 25)

