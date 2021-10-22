import math
from typing import List

from src.classes.color import *


class Canvas:

    def __init__(self, width, height, initial_color=Color(0, 0, 0)):
        self.grid = [[initial_color for i in range(width)] for o in range(height)]

    def write_pixel(self, width: int, height: int, c: Color) -> None:
        self.grid[height][width] = c

    def write_pixel_float(self, width: float, height: float, c: Color) -> None:
        self.write_pixel(math.floor(width), math.floor(height), c)

    def pixel_at(self, width: int, height: int) -> Color:
        return self.grid[height][width]

    def width(self) -> int:
        return len(self.grid[0])

    def height(self) -> int:
        return len(self.grid)

    def scale(self, value: int) -> List[List[Color]]:
        scaled_grid = self.grid.copy()
        for i in range(len(scaled_grid)):
            for o in range(len(scaled_grid[0])):
                scaled_grid[i][o] = scaled_grid[i][o] * value
        return scaled_grid


def canvas_to_ppm(c: Canvas):
    max_pixel_val: int = 255
    width = c.width()
    height = c.height()
    header: str = "P3\n" \
                  f"{width} {height}\n" \
                  f"{max_pixel_val}\n"

    scaled_canvas = c.scale(max_pixel_val)
    image: str = ""

    row = 0
    for i in range(height):
        for o in range(width):
            pixel = c.pixel_at(o, i)
            image += color_to_ppm(pixel, max_pixel_val)
        image = image.rstrip()
        image += "\n"

    image = restrict_line_length(image)

    return header + image


def restrict_line_length(image: str) -> str:
    max_line_length: int = 70
    lines = image.splitlines()
    final_image = ""

    count = 0
    while count < len(lines):
        line = lines[count]
        if len(line) > max_line_length:
            cutoff = find_cutoff(line, max_line_length)
            remainder = line[cutoff + 1:]
            lines.insert(count + 1, remainder)
            line = line[:cutoff]
        final_image += line + "\n"
        count += 1

    return final_image


def find_cutoff(line: str, max_chars: int) -> int:
    index = line.rindex(" ")
    while index > max_chars - 1:
        index = line.rindex(" ", 0, index)
    return index


def collapse_value(v: float, max_val: int) -> int:
    value = math.ceil(v)
    if value > max_val:
        return max_val
    if value < 0:
        return 0
    return value


def color_to_ppm(c: Color, max_value: int) -> str:
    return f"{collapse_value(c.red(), max_value)} {collapse_value(c.green(), max_value)} {collapse_value(c.blue(), max_value)} "


def write_canvas_to_file(c: Canvas, name: str) -> None:
    ppm = canvas_to_ppm(c)

    with open(f"../build/{name}.ppm", "w") as file:
        file.flush()
        file.write(ppm)
