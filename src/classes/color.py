from src.classes.tuple import Tuple


class Color:

    def __init__(self, red: float, green: float, blue: float) -> None:
        self.tuple = Tuple(red, green, blue, 0)

    def red(self) -> float:
        return self.tuple.x

    def green(self) -> float:
        return self.tuple.y

    def blue(self) -> float:
        return self.tuple.z

    def __add__(self, other):
        return color_from_tuple(self.tuple + other.tuple)

    def __sub__(self, other):
        return color_from_tuple(self.tuple - other.tuple)

    def __mul__(self, scalar:float):
        return color_from_tuple(self.tuple*scalar)

    def __eq__(self, other) -> bool:
        return self.tuple == other.tuple

    def __str__(self) -> str:
        return f"(red: {self.red()}, green: {self.green()}, blue: {self.blue()})"


def color_from_tuple(t: Tuple) -> Color:
    return Color(t.x, t.y, t.z)


def hp(c1: Color, c2: Color) -> Color:
    # hadamard product
    return Color(c1.red() * c2.red(),
                 c1.green() * c2.green(),
                 c1.blue() * c2.blue())