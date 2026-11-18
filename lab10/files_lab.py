def read_matrix(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        raise ValueError("Файл пустой")

    lines = text.splitlines()

    # --- заголовок (строка 1) ---
    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError("Строка 1: в заголовке должно быть ровно два числа")
    try:
        n_rows = int(header_parts[0])
        n_cols = int(header_parts[1])
    except ValueError:
        raise ValueError("Строка 1: заголовок содержит не целые числа")
    if n_rows <= 0 or n_cols <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    # --- проверка количества строк данных ---
    data_lines = lines[1:]
    # Пустые строки где-либо — ошибка
    for i, line in enumerate(data_lines, start=2):
        if line.strip() == "":
            raise ValueError(f"Строка {i}: пустая строка")

    if len(data_lines) != n_rows:
        if len(data_lines) > n_rows:
            raise ValueError(
                f"Ожидалось {n_rows} строк данных, получено {len(data_lines)}"
            )
        raise ValueError(
            f"Ожидалось {n_rows} строк данных, получено {len(data_lines)}"
        )


    matrix = []
    for i, line in enumerate(data_lines, start=2):
        parts = line.split()
        if len(parts) != n_cols:
            raise ValueError(
                f"Строка {i}: ожидалось {n_cols} чисел, получено {len(parts)}"
            )
        row = []
        for j, token in enumerate(parts, start=1):
            try:
                row.append(int(token))
            except ValueError:
                raise ValueError(
                    f"Строка {i}, столбец {j}: нечисловое значение '{token}'"
                )
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    total = 0
    for row in matrix:
        for x in row:
            if x % 3 == 0:
                total += x
    return total


def export_to_csv(matrix, path):
    import csv
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in matrix:
            writer.writerow(row)