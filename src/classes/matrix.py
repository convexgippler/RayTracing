from typing import List
from src.classes.tuple import Tuple
import numpy as np
from main import EPSILON


class Matrix:

    def __init__(self, matrix):
        self.matrix: np.ndarray = np.array(matrix,dtype=float)

    def __getitem__(self, pos) -> float:
        row, column = pos
        return self.matrix[row, column]

    def __setitem__(self, pos: (int, int), value: float):
        row, column = pos
        self.matrix[row, column] = value

    def __eq__(self, o) -> bool:
        return np.allclose(self.matrix, o.matrix, atol=EPSILON)

    def __mul__(self, other):
        height, _ = self.matrix.shape
        _, width = other.matrix.shape
        result = np.empty_like(None, shape=(height, width), dtype=float)
        for row in range(height):
            for column in range(width):
                a = np.multiply(self.matrix[row], other.matrix[:, column])
                result[row, column] = np.sum(a)
        return Matrix(result)

    def size(self):
        size, _ = self.matrix.shape
        return size

    def get_column_as_tuple(self, col: int):
        column = self.matrix[:, col]
        return Tuple(
            column[0],
            column[1],
            column[2],
            column[3],
        )

    def transpose(self):
        new_matrix = np.empty_like(self.matrix)
        height, width = self.matrix.shape
        for row in range(height):
            for column in range(width):
                new_matrix[column, row] = self[row, column]
        return Matrix(new_matrix)

    def submatrix(self, row, column):
        sub = self.matrix.copy()
        sub = np.delete(sub, row, 0)
        return Matrix(np.delete(sub, column, 1))

    def like(self):
        return Matrix(np.empty_like(self.matrix))


def matrix_from_tuple(t: Tuple) -> Matrix:
    return Matrix([
        [t.x],
        [t.y],
        [t.z],
        [t.w],
    ])


def matrix_rows(row0: List[float] = None, row1: List[float] = None, row2: List[float] = None,
                row3: List[float] = None) -> Matrix:
    table = []
    if row0 is not None:
        table.append(row0)
        if row1 is not None:
            table.append(row1)
            if row2 is not None:
                table.append(row2)
                if row3 is not None:
                    table.append(row3)
    return Matrix(table)


def identity_matrix(size: int) -> Matrix:
    matrix = Matrix([[0 for i in range(size)] for o in range(size)])
    for i in range(size):
        matrix[i, i] = 1
    return matrix


IDENTITY = identity_matrix(4)


def multiply_matrix_tuple(m: Matrix, t: Tuple) -> Tuple:
    m2 = matrix_from_tuple(t)
    result = m * m2
    return result.get_column_as_tuple(0)


def determinant(m: Matrix) -> int:
    if m.size() == 2:
        return m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]

    det = 0
    for col in range(m.size()):
        det += m[0, col] * cofactor(m, 0, col)
    return det


def minor(m: Matrix, row: int, column: int) -> int:
    return determinant(m.submatrix(row, column))


def cofactor(m: Matrix, row: int, column: int) -> int:
    return minor(m, row, column) * (1 - 2 * ((row + column) % 2))


def is_reversible(m: Matrix) -> bool:
    return determinant(m) != 0


def inverse(m: Matrix) -> Matrix:
    if not is_reversible(m):
        raise ValueError('Matrix is not reversible.')

    inv = m.like()
    size = m.size()
    det = determinant(m)

    for row in range(size):
        for col in range(size):
            c = cofactor(m, row, col)
            inv[col, row] = c / det

    return inv
