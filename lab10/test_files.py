import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix, selected_sum


class TestReadMatrix(unittest.TestCase):
    def _write(self, directory, name, content):
        path = Path(directory) / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_matrix(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "1 2\n7 -1\n")
            self.assertEqual(read_matrix(path), [[7, -1]])

    def test_1x1_zero(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "1 1\n0\n")
            self.assertEqual(read_matrix(path), [[0]])

    def test_empty_file(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "")
            try:
                read_matrix(path)
            except ValueError:
                pass
            else:
                self.fail("Пустой файл не вызвал ValueError")

    def test_zero_in_header(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "0 3\n")
            try:
                read_matrix(path)
            except ValueError:
                pass
            else:
                self.fail("Заголовок 0 3 не вызвал ValueError")

    def test_wrong_column_count(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "1 2\n1\n")
            try:
                read_matrix(path)
            except ValueError as e:
                self.assertIn("2", str(e))  # строка 2
            else:
                self.fail("Неверное количество столбцов не вызвало ошибку")

    def test_non_numeric_cell(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "1 2\n1 x\n")
            try:
                read_matrix(path)
            except ValueError as e:
                self.assertIn("2", str(e))  # строка 2
            else:
                self.fail("Нечисловая ячейка не вызвала ошибку")

    def test_extra_data_lines(self):
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "1 1\n5\n6\n")
            try:
                read_matrix(path)
            except ValueError:
                pass
            else:
                self.fail("Лишняя строка данных не вызвала ошибку")

    def test_missing_file(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "no_such_file.txt"
            with self.assertRaises(FileNotFoundError):
                read_matrix(path)

    def test_trailing_newline_ok(self):
        # Один перевод строки в конце — допустим
        with TemporaryDirectory() as d:
            path = self._write(d, "m.txt", "1 2\n7 -1\n")
            self.assertEqual(read_matrix(path), [[7, -1]])


class TestSelectedSum(unittest.TestCase):
    def test_variant_5(self):
        # Вариант 5: элементы, кратные 3
        matrix = [[1, -2, 3], [4, 0, -6]]
        # 3 + 0 + (-6) = -3
        self.assertEqual(selected_sum(matrix), -3)

    def test_empty_matrix(self):
        self.assertEqual(selected_sum([]), 0)

    def test_no_multiples_of_3(self):
        self.assertEqual(selected_sum([[1, 2], [4, 5]]), 0)


if __name__ == "__main__":
    unittest.main()