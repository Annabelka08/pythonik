from table import row_sums, column_sums, diagonal_pattern, transform


def read_matrix():
    print("Вводите строки матрицы по одной, числа через пробел.")
    print("Пустая строка — завершить ввод.")
    matrix = []
    expected_cols = None
    while True:
        line = input().strip()
        if not line:
            break
        try:
            row = list(map(int, line.split()))
        except ValueError:
            print("Ошибка: нужны целые числа. Повторите строку.")
            continue
        if expected_cols is None:
            expected_cols = len(row)
        elif len(row) != expected_cols:
            print(f"Ошибка: ожидалось {expected_cols} столбцов, получено {len(row)}.")
            continue
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))


def main():
    matrix = read_matrix()

    print("\nИсходная матрица:")
    print_matrix(matrix)

    print("\nСуммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    # Диагональный узор
    while True:
        try:
            size = int(input("\nВведите положительный размер узора: "))
            if size >= 1:
                break
            print("Размер должен быть >= 1.")
        except ValueError:
            print("Нужно целое число.")

    pattern = diagonal_pattern(size)
    print(f"\nДиагональный узор {size}x{size}:")
    print_matrix(pattern)

    # Преобразование (вариант 5)
    transformed = transform(matrix)
    print("\nПреобразованная матрица (отрицательные → модули):")
    print_matrix(transformed)


if __name__ == "__main__":
    main()