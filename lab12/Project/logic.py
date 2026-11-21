def validate_records(records):
    if not isinstance(records, list):
        raise ValueError("Корневой элемент должен быть списком.")

    seen_ids = set()
    for rec in records:
        if not isinstance(rec, dict):
            raise ValueError("Каждая запись должна быть словарём.")

        required_keys = {"id", "title", "category", "amount", "completed"}
        if not required_keys.issubset(rec.keys()):
            raise ValueError(f"Запись {rec.get('id', '?')} не содержит всех обязательных ключей.")

        rec_id = rec["id"]
        if not isinstance(rec_id, int) or isinstance(rec_id, bool) or rec_id <= 0:
            raise ValueError("ID должен быть положительным целым числом.")
        if rec_id in seen_ids:
            raise ValueError(f"Повторяющийся ID: {rec_id}")
        seen_ids.add(rec_id)

        for field in ["title", "category"]:
            val = rec[field]
            if not isinstance(val, str) or not val.strip():
                raise ValueError(f"Поле '{field}' должно быть непустой строкой.")

        amt = rec["amount"]
        if not isinstance(amt, int) or isinstance(amt, bool) or amt < 0:
            raise ValueError("Поле 'amount' (количество уроков) должно быть целым неотрицательным числом.")

        if not isinstance(rec["completed"], bool):
            raise ValueError("Поле 'completed' должно быть строго типа bool.")

    return True


def add_record(records, title, category, amount):
    new_id = max((rec["id"] for rec in records), default=0) + 1
    new_record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False
    }
    records.append(new_record)
    return new_record


def find_records(records, query):
    if not query.strip():
        return []
    q = query.strip().lower()
    return [rec for rec in records if q in rec["title"].lower()]


def set_completed(records, record_id, completed):
    for rec in records:
        if rec["id"] == record_id:
            rec["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    for i, rec in enumerate(records):
        if rec["id"] == record_id:
            del records[i]
            return True
    return False


def statistics(records):
    total = len(records)
    completed_count = sum(1 for rec in records if rec["completed"])
    not_completed_count = total - completed_count
    total_amount = sum(rec["amount"] for rec in records)

    categories = {}
    for rec in records:
        cat = rec["category"].strip()
        categories[cat] = categories.get(cat, 0) + rec["amount"]

    sorted_categories = dict(sorted(categories.items()))

    return {
        "total": total,
        "completed": completed_count,
        "not_completed": not_completed_count,
        "total_amount": total_amount,
        "categories": sorted_categories
    }