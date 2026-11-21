import json
import os
from logic import validate_records


def load_records(path):
    if not os.path.exists(path):
        print(f"Файл {path} не найден. Начинаем с пустого списка курсов.")
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка формата JSON: {e}")
    except UnicodeDecodeError as e:
        raise ValueError(f"Ошибка кодировки файла: {e}")

    validate_records(data)
    return data


def save_records(path, records):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False