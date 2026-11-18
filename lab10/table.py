def row_sums(matrix):
    return [sum(row) for row in matrix]


def column_sums(matrix):
    if not matrix:
        return []
    n_cols = len(matrix[0])
    return [sum(matrix[r][c] for r in range(len(matrix)))
            for c in range(n_cols)]


def diagonal_pattern(size):
        return [
        [0 if r == c else (1 if r < c else 2) for c in range(size)]
        for r in range(size)
    ]


def transform(matrix):
        return [[abs(x) if x < 0 else x for x in row] for row in matrix]
