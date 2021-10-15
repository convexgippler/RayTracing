from math import sqrt


class Tuple:

    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z
        self.w: float = w

    def is_vector(self) -> bool:
        return self.w == 0.0

    def is_point(self) -> bool:
        return self.w == 1.0

    def dot(self, other) -> float:
        return dot(self, other)

    def __add__(self, other):
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __neg__(self):
        return Tuple(0, 0, 0, 0) - self

    def __mul__(self, scalar: float):
        return Tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def __truediv__(self, scalar: float):
        return self * (1 / scalar)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __eq__(self, o) -> bool:
        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w


def point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0.0)


def magnitude(v: Tuple) -> float:
    return sqrt(pow(v.x, 2) + pow(v.y, 2) + pow(v.z, 2) + pow(v.w, 2))


def normalize(v: Tuple) -> Tuple:
    return v / magnitude(v)


def dot(v1: Tuple, v2: Tuple) -> float:
    return v1.x * v2.x + \
           v1.y * v2.y + \
           v1.z * v2.z + \
           v1.w * v2.w


def cross(v1: Tuple, v2: Tuple) -> Tuple:
    return vector(v1.y * v2.z - v1.z * v2.y,
                  v1.z * v2.x - v1.x * v2.z,
                  v1.x * v2.y - v1.y * v2.x)
