import unittest
from table import row_sums, column_sums, diagonal_pattern, transform


class TestSums(unittest.TestCase):
    def test_2x3(self):
        m = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(row_sums(m), [6, 15])
        self.assertEqual(column_sums(m), [5, 7, 9])

    def test_1x1(self):
        m = [[7]]
        self.assertEqual(row_sums(m), [7])
        self.assertEqual(column_sums(m), [7])

    def test_column_vector(self):
        m = [[1], [-1], [0]]
        self.assertEqual(row_sums(m), [1, -1, 0])
        self.assertEqual(column_sums(m), [0])

    def test_empty(self):
        self.assertEqual(row_sums([]), [])
        self.assertEqual(column_sums([]), [])


class TestDiagonalPattern(unittest.TestCase):
    def test_size_1(self):
        self.assertEqual(diagonal_pattern(1), [[0]])

    def test_size_3(self):
        expected = [
            [0, 1, 1],
            [2, 0, 1],
            [2, 2, 0],
        ]
        self.assertEqual(diagonal_pattern(3), expected)


class TestTransform(unittest.TestCase):
    def setUp(self):
        self.original = [[-2, 0, 3], [4, -5, 6]]

    def test_variant_5(self):
        self.assertEqual(transform(self.original),
                         [[2, 0, 3], [4, 5, 6]])

    def test_empty(self):
        self.assertEqual(transform([]), [])

    def test_original_not_mutated(self):
        result = transform(self.original)
        result[0][0] = 999
        self.assertEqual(self.original, [[-2, 0, 3], [4, -5, 6]])


if __name__ == "__main__":
    unittest.main()