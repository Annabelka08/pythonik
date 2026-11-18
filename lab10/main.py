from pathlib import Path
from files_lab import read_matrix, selected_sum, export_to_csv
from table import row_sums, column_sums


def read_positive_integer(prompt="Введите положительное целое число: "):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print("Ошибка: это не целое число. Попробуйте ещё раз.")
            continue
        if number <= 0:
            print("Ошибка: число должно быть больше нуля. Попробуйте ещё раз.")
            continue
        return number


def main():
    input_path = Path("matrix.txt")
    report_path = Path("report.txt")
    csv_path = Path("matrix.csv")

    # --- чтение и проверка входа ---
    try:
        matrix = read_matrix(input_path)
    except FileNotFoundError:
        print(f"Файл {input_path} не найден.")
        return
    except UnicodeDecodeError:
        print(f"Файл {input_path} имеет неверную кодировку (ожидается UTF-8).")
        return
    except ValueError as e:
        print(f"Ошибка формата файла {input_path}: {e}")
        return
    except OSError as e:
        print(f"Ошибка доступа к файлу {input_path}: {e}")
        return

    # --- вычисления ---
    r_sums = row_sums(matrix)
    c_sums = column_sums(matrix)
    variant_result = selected_sum(matrix)

    # --- запись отчёта (только после успешной проверки) ---
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("Суммы строк: " + " ".join(str(x) for x in r_sums) + "\n")
            f.write("Суммы столбцов: " + " ".join(str(x) for x in c_sums) + "\n")
            f.write(f"Результат варианта: {variant_result}\n")
    except OSError as e:
        print(f"Не удалось записать отчёт: {e}")
        return

    # --- экспорт в CSV ---
    try:
        export_to_csv(matrix, csv_path)
    except OSError as e:
        print(f"Не удалось записать CSV: {e}")
        return

    print(f"Отчёт записан в {report_path}")
    print(f"CSV экспортирован в {csv_path}")

    # --- запрос размера для узора ---
    size = read_positive_integer("Введите размер диагонального узора: ")
    from table import diagonal_pattern
    pattern = diagonal_pattern(size)
    for row in pattern:
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    main()
