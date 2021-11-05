from typing import List
from src.classes.tuple import Tuple
import numpy as np
from main import EPSILON


class Matrix:

    def __init__(self, matrix: List[List[float]]):
        self.matrix: np.ndarray = np.array(matrix)

    def __getitem__(self, pos) -> float:
        row, column = pos
        return self.matrix[row, column]

    def __setitem__(self, pos: (int, int), value: int) -> float:
        row, column = pos
        self.matrix[row, column] = value

    def __eq__(self, o: object) -> bool:
        return np.allclose(self.matrix, o.matrix, atol=EPSILON)

    def __mul__(self, other):
        height, unused = self.matrix.shape
        unused, width = other.matrix.shape
        result = np.empty_like(None, shape=(height, width), dtype=float)
        for row in range(height):
            for column in range(width):
                a = np.multiply(self.matrix[row], other.matrix[:, column])
                result[row, column] = np.sum(a)
        return Matrix(result)

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
        height,width = self.matrix.shape
        for row in range(height):
            for column in range(width):
                new_matrix[column,row] = self[row,column]
        return Matrix(new_matrix)



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


def multiply_matrix_tuple(m: Matrix, t: Tuple)-> Tuple:
    m2 = matrix_from_tuple(t)
    result = m * m2
    return result.get_column_as_tuple(0)

def determinant(m: Matrix)->int:
    return m[0,0]*m[1,1] - m[0,1]*m[1,0]

