import unittest
from src.classes.canvas import *


class CanvasTest(unittest.TestCase):

    def test_creating_canvas(self):
        # Scenario: Creating a canvas
        c = Canvas(10, 20)
        self.assertEqual(10, c.width())
        self.assertEqual(20, c.height())
        black = Color(0, 0, 0)
        for i in range(10):
            for o in range(20):
                self.assertEqual(black, c.pixel_at(i, o))

    def test_write_pixel(self):
        # Scenario: Writing pixels to a canvas
        c = Canvas(10, 20)
        red = Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertEqual(red, c.pixel_at(2, 3))

    def test_header(self):
        # Scenario: Constructing the PPM header
        c = Canvas(5, 3)
        ppm = canvas_to_ppm(c)
        lines = ppm.splitlines()
        self.assertEqual("P3", lines[0])
        self.assertEqual("5 3", lines[1])
        self.assertEqual("255", lines[2])

    def test_pixel_data(self):
        # Scenario: Constructing the PPM pixel data
        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = canvas_to_ppm(c)
        lines = ppm.splitlines()
        self.assertEqual("255 0 0 0 0 0 0 0 0 0 0 0 0 0 0", lines[3])
        self.assertEqual("0 0 0 0 0 0 0 128 0 0 0 0 0 0 0", lines[4])
        self.assertEqual("0 0 0 0 0 0 0 0 0 0 0 0 0 0 255", lines[5])

    def test_line_length_limit(self):
        # Scenario: Splitting long lines in PPM files
        c = Canvas(10, 2, Color(1, 0.8, 0.6))
        ppm = canvas_to_ppm(c)
        lines = ppm.splitlines()
        self.assertEqual("255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204", lines[3])
        self.assertEqual("153 255 204 153 255 204 153 255 204 153 255 204 153", lines[4])
        self.assertEqual("255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204", lines[5])
        self.assertEqual("153 255 204 153 255 204 153 255 204 153 255 204 153", lines[6])

    def test_ppm_newline_end(self):
        # Scenario: PPM files are terminated by a newline character
        c = Canvas(5, 3)
        ppm = canvas_to_ppm(c)
        self.assertEqual("\n", ppm[-1])
