import unittest
import tempfile
import os
from storage import load_records, save_records

class TestStorage(unittest.TestCase):
    def test_save_and_load(self):
        data = [{"id": 1, "title": "Test Course", "category": "IT", "amount": 5, "completed": True}]
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "test.json")
            self.assertTrue(save_records(path, data))
            loaded = load_records(path)
            self.assertEqual(loaded, data)

    def test_load_missing_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "missing.json")
            self.assertEqual(load_records(path), [])

    def test_load_broken_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "broken.json")
            with open(path, "w", encoding="utf-8") as f:
                f.write("{broken json")
            with self.assertRaises(ValueError):
                load_records(path)

if __name__ == '__main__':
    unittest.main()