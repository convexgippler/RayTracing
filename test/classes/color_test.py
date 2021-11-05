import unittest
from src.classes.color import *


class ColorTest(unittest.TestCase):

    def test_color_creation(self):
        # Scenario: Colors are (red, green, blue) tuples
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(-0.5, c.red())
        self.assertEqual(0.4, c.green())
        self.assertEqual(1.7, c.blue())

    def test_add_colors(self):
        # Scenario: Adding colors
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(Color(1.6, 0.7, 1.0), c1 + c2)

    def test_subtract_colors(self):
        # Given c1 ← color(0.9, 0.6, 0.75)
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(Color(0.2, 0.5, 0.5), c1 - c2)

    def test_multiply_color_scalar(self):
        # Scenario: Multiplying a color by a scalar
        c = Color(0.2, 0.3, 0.4)
        self.assertEqual(Color(0.4, 0.6, 0.8), c * 2)

    def test_multiply_colors(self):
        # Scenario: Multiplying colors
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertEqual(Color(0.9, 0.2, 0.04), hp(c1, c2))
