import unittest

from src.classes.tuple import *


class Tuple_Test(unittest.TestCase):

    def test_tuple_point(self):
        # Scenario: A tuple with w=1.0 is a point
        a: Tuple = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertAlmostEqual(4.3, a.x)
        self.assertAlmostEqual(-4.2, a.y)
        self.assertAlmostEqual(3.1, a.z)
        self.assertAlmostEqual(1.0, a.w)
        self.assertTrue(a.is_point())
        self.assertFalse(a.is_vector())

    def test_tuple_vector(self):
        # Scenario: A tuple with w=0 is a vector
        a: Tuple = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertAlmostEqual(4.3, a.x)
        self.assertAlmostEqual(-4.2, a.y)
        self.assertAlmostEqual(3.1, a.z)
        self.assertAlmostEqual(0.0, a.w)
        self.assertFalse(a.is_point())
        self.assertTrue(a.is_vector())

    def test_point(self):
        # Scenario: point() creates tuples with w=1
        a = point(4, -4, 3)
        self.assertEqual(Tuple(4, -4, 3, 1), a)

    def test_vector(self):
        # Scenario: vector() creates tuples with w=0
        a = vector(4, -4, 3)
        self.assertEqual(Tuple(4, -4, 3, 0), a)

    def test_add(self):
        # Scenario: Adding two tuples
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(Tuple(1, 1, 6, 1), a1 + a2)

    def test_subtract_points(self):
        # Scenario: Subtracting two points
        a1 = point(3, 2, 1)
        a2 = point(5, 6, 7)
        self.assertEqual(vector(-2, -4, -6), a1 - a2)

    def test_subtract_vector_from_point(self):
        # Scenario: Subtracting a vector from a point
        p = point(3, 2, 1)
        v = vector(5, 6, 7)
        self.assertEqual(point(-2, -4, -6), p - v)

    def test_subtract_vectors(self):
        # Scenario: Subtracting two vectors
        v1 = vector(3, 2, 1)
        v2 = vector(5, 6, 7)
        self.assertEqual(vector(-2, -4, -6), v1 - v2)

    def test_subtracting_vector_from_zero(self):
        # Scenario: Subtracting a vector from the zero vector
        zero = vector(0, 0, 0)
        v = vector(1, -2, 3)
        self.assertEqual(vector(-1, 2, -3), zero - v)

    def test_negating_tuple(self):
        # Scenario: Negating a tuple
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(-1, 2, -3, 4), -a)

    def test_multiply_tuple_scalar(self):
        # Scenario: Multiplying a tuple by a scalar
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(3.5, -7, 10.5, -14), a * 3.5)

    def test_multiply_tuple_fraction(self):
        # Scenario: Multiplying a tuple by a fraction
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(0.5, -1, 1.5, -2), a * 0.5)

    def test_divide_tuple_scalar(self):
        # Scenario: Dividing a tuple by a scalar
        a = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(0.5, -1, 1.5, -2), a / 2)

    def test_magnitude(self):
        # Scenario: Computing the magnitude of vector(1, 0, 0)
        v = vector(1, 0, 0)
        self.assertEqual(1, magnitude(v))
        # Scenario: Computing the magnitude of vector(0, 0, 1)
        v = vector(0, 0, 1)
        self.assertEqual(1, magnitude(v))
        # Scenario: Computing the magnitude of vector(1, 2, 3)
        v = vector(1, 2, 3)
        self.assertEqual(sqrt(14), magnitude(v))
        # Scenario: Computing the magnitude of vector(-1, -2, -3)
        v = vector(-1, -2, -3)
        self.assertEqual(sqrt(14), magnitude(v))

    def test_normalize(self):
        # Scenario: Normalizing vector(4, 0, 0) gives (1, 0, 0)
        v = vector(4, 0, 0)
        self.assertEqual(vector(1, 0, 0), normalize(v))
        # Scenario: Normalizing vector(1, 2, 3)
        v = vector(1, 2, 3)
        self.assertEqual(vector(1 / sqrt(14), 2 / sqrt(14), 3 / sqrt(14)), normalize(v))

    def test_normalized_magnitude(self):
        # Scenario: The magnitude of a normalized vector
        v = vector(1, 2, 3)
        norm = normalize(v)
        self.assertEqual(1, magnitude(norm))

    def test_dot_product(self):
        # Scenario: The dot product of two tuples
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(20, dot(a, b))

    def test_cross_product(self):
        # Scenario: The cross product of two vectors
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        self.assertEqual(vector(-1, 2, -1), cross(a, b))
        self.assertEqual(vector(1, -2, 1), cross(b, a))
