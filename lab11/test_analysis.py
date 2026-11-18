import unittest
import copy
from analysis import validate_todos, completion_counts, top_users, select_tasks


class TestValidation(unittest.TestCase):
    def test_valid(self):
        data = [{"id": 1, "userId": 5, "title": "Test", "completed": True, "extra": "ok"}]
        validate_todos(data)  # Не должно выбрасывать исключений

    def test_not_list(self):
        with self.assertRaisesRegex(ValueError, "списком"):
            validate_todos({})

    def test_duplicate_id(self):
        data = [
            {"id": 1, "userId": 5, "title": "A", "completed": True},
            {"id": 1, "userId": 5, "title": "B", "completed": False}
        ]
        with self.assertRaisesRegex(ValueError, "повторяющийся"):
            validate_todos(data)

    def test_missing_userid(self):
        data = [{"id": 1, "title": "A", "completed": True}]
        with self.assertRaisesRegex(ValueError, "userId"):
            validate_todos(data)

    def test_completed_not_bool(self):
        data = [{"id": 1, "userId": 5, "title": "A", "completed": "false"}]
        with self.assertRaisesRegex(ValueError, "bool"):
            validate_todos(data)

    def test_id_is_bool(self):
        data = [{"id": True, "userId": 5, "title": "A", "completed": True}]
        with self.assertRaisesRegex(ValueError, "целым числом"):
            validate_todos(data)


class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.todos = [
            {"id": 1, "userId": 5, "title": "A", "completed": True},
            {"id": 2, "userId": 5, "title": "B", "completed": False},
            {"id": 3, "userId": 10, "title": "C", "completed": True},
            {"id": 4, "userId": 10, "title": "D", "completed": True},
            {"id": 5, "userId": 5, "title": "E", "completed": True}
        ]
        self.original_todos = copy.deepcopy(self.todos)

    def test_completion_counts(self):
        counts = completion_counts(self.todos)
        self.assertEqual(counts, {5: 2, 10: 2})
        self.assertEqual(self.todos, self.original_todos)  # Неизменность

    def test_top_users(self):
        counts = {5: 2, 10: 2, 1: 0}
        self.assertEqual(top_users(counts), [5, 10])

        self.assertEqual(top_users({}), [])
        self.assertEqual(top_users({1: 0, 2: 0}), [])

    def test_select_tasks_variant_5(self):
        # Вариант 5: id <= parameter
        res = select_tasks(self.todos, 5, parameter=2)
        self.assertEqual(res, [1, 2])

        res_unknown = select_tasks(self.todos, 99, parameter=2)
        self.assertEqual(res_unknown, [])

        res_no_match = select_tasks(self.todos, 5, parameter=0)
        self.assertEqual(res_no_match, [])
        self.assertEqual(self.todos, self.original_todos)


if __name__ == "__main__":
    unittest.main()