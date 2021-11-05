import unittest
from src.classes.matrix import *
from src.classes.tuple import *


class MatrixTest(unittest.TestCase):

    def test_create_4x4_matrix(self):
        # Scenario: Constructing and inspecting a 4x4 matrix
        m = Matrix([
            [1, 2, 3, 4],
            [5.5, 6.5, 7.5, 8.5],
            [9, 10, 11, 12],
            [13.5, 14.5, 15.5, 16.5]
        ])

        self.assertEqual(m[0, 0], 1)
        self.assertEqual(m[0, 3], 4)
        self.assertEqual(m[1, 0], 5.5)
        self.assertEqual(m[1, 2], 7.5)
        self.assertEqual(m[2, 2], 11)
        self.assertEqual(m[3, 0], 13.5)
        self.assertEqual(m[3, 2], 15.5)

    def test_create_2x2_matrix(self):
        # Given the following 2x2 matrix M:
        m = Matrix([
            [-3, 5],
            [1, -2]
        ])
        self.assertEqual(m[0, 0], -3)
        self.assertEqual(m[0, 1], 5)
        self.assertEqual(m[1, 0], 1)
        self.assertEqual(m[1, 1], -2)

    def test_create_3x3_matrix(self):
        # Scenario: A 3x3 matrix ought to be representable
        m = Matrix([
            [-3, 5, 0],
            [1, -2, -7],
            [0, 1, 1],
        ])
        self.assertEqual(m[0, 0], -3)
        self.assertEqual(m[1, 1], -2)
        self.assertEqual(m[2, 2], 1)

    def test_matrix_equality(self):
        # Scenario: Matrix equality with identical matrices
        A = Matrix([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 8, 7, 6],
            [5, 4, 3, 2]
        ])
        B = Matrix([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 8, 7, 6],
            [5, 4, 3, 2],
        ])
        self.assertTrue(A == B)

    def test_matrix_inequality(self):
        # Scenario: Matrix equality with different matrices
        A = Matrix([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 8, 7, 6],
            [5, 4, 3, 2],
        ])
        B = Matrix([
            [2, 3, 4, 5],
            [6, 7, 8, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1]
        ])
        self.assertFalse(A == B)

    def test_matrix_multiplication(self):
        # Scenario: Multiplying two matrices
        A = Matrix([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 8, 7, 6],
            [5, 4, 3, 2],
        ])
        B = Matrix([
            [-2, 1, 2, 3],
            [3, 2, 1, -1],
            [4, 3, 6, 5],
            [1, 2, 7, 8],
        ])
        self.assertEqual(
            Matrix([
                [20, 22, 50, 48],
                [44, 54, 114, 108],
                [40, 58, 110, 102],
                [16, 26, 46, 42],
            ]),
            A * B
        )

    def test_matrix_multiplied_by_tuple(self):
        # Scenario: A matrix multiplied by a tuple
        A = Matrix([
            [1, 2, 3, 4],
            [2, 4, 4, 2],
            [8, 6, 4, 1],
            [0, 0, 0, 1],
        ])
        B = Tuple(1, 2, 3, 1)
        self.assertEqual(Tuple(18, 24, 33, 1), multiply_matrix_tuple(A, B))

    def test_identity_multiplication(self):
        # Scenario: Multiplying a matrix by the identity matrix
        A = Matrix([
            [0, 1, 2, 4],
            [1, 2, 4, 8],
            [2, 4, 8, 16],
            [4, 8, 16, 32],
        ])
        self.assertEqual(A, A * IDENTITY)

    def test_transposition(self):
        a = Matrix([
            [0, 9, 3, 0],
            [9, 8, 0, 8],
            [1, 8, 5, 3],
            [0, 0, 5, 8],
        ])
        t = Matrix([
            [0, 9, 1, 0],
            [9, 8, 8, 0],
            [3, 0, 5, 5],
            [0, 8, 3, 8],
        ])
        self.assertEqual(t, a.transpose())

    def test_transpose_identity(self):
        # Scenario: Transposing the identity matrix
        self.assertEqual(IDENTITY, IDENTITY.transpose())

    def test_determinant(self):
        # Scenario: Calculating the determinant of a 2x2 matrix
        A = Matrix([
            [1,5],
            [-3,2]
        ])
        self.assertEqual(17,determinant(A))
