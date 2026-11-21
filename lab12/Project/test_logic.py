import unittest
from logic import validate_records, add_record, find_records, set_completed, delete_record, statistics

class TestLogic(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"id": 1, "title": "Python для начинающих", "category": "Программирование", "amount": 15, "completed": False},
            {"id": 2, "title": "Основы дизайна", "category": "Дизайн", "amount": 8, "completed": True}
        ]

    def test_validate_correct(self):
        self.assertTrue(validate_records(self.records))

    def test_validate_bad_amount(self):
        bad = [{"id": 1, "title": "A", "category": "B", "amount": -5, "completed": False}]
        with self.assertRaises(ValueError):
            validate_records(bad)

    def test_add_record(self):
        new = add_record(self.records, "  Новый курс  ", "  Языки ", 10)
        self.assertEqual(new["id"], 3)
        self.assertEqual(new["title"], "Новый курс")
        self.assertEqual(new["category"], "Языки")
        self.assertEqual(len(self.records), 3)

    def test_find_case_insensitive(self):
        found = find_records(self.records, "python")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["id"], 1)

    def test_set_completed_unknown(self):
        self.assertFalse(set_completed(self.records, 99, True))

    def test_delete_record(self):
        self.assertTrue(delete_record(self.records, 1))
        self.assertEqual(len(self.records), 1)
        self.assertEqual(self.records[0]["id"], 2)

    def test_statistics(self):
        stats = statistics(self.records)
        self.assertEqual(stats["total"], 2)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["not_completed"], 1)
        self.assertEqual(stats["total_amount"], 23)
        self.assertEqual(stats["categories"]["Программирование"], 15)
        self.assertEqual(stats["categories"]["Дизайн"], 8)

if __name__ == '__main__':
    unittest.main()