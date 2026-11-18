def row_sums(matrix):
    return [sum(row) for row in matrix]


def column_sums(matrix):
    if not matrix:
        return []
    n_cols = len(matrix[0])
    return [sum(matrix[row][col] for row in range(len(matrix)))
            for col in range(n_cols)]


def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        current_row = []
        for col in range(size):
            if row == col:
                current_row.append(0)
            elif row < col:
                current_row.append(1)
            else:
                current_row.append(2)
        matrix.append(current_row)
    return matrix


def transform(matrix):
    return [[abs(x) if x < 0 else x for x in row] for row in matrix]