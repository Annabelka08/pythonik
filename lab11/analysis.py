def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Корневой элемент должен быть списком")

    seen_ids = set()
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i}: должен быть словарём")

        # Проверка id
        if "id" not in item or type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Элемент {i}: 'id' должен быть положительным целым числом")
        if item["id"] in seen_ids:
            raise ValueError(f"Элемент {i}: повторяющийся 'id' {item['id']}")
        seen_ids.add(item["id"])

        # Проверка userId
        if "userId" not in item or type(item["userId"]) is not int or item["userId"] <= 0:
            raise ValueError(f"Элемент {i}: 'userId' должен быть положительным целым числом")

        # Проверка title
        if "title" not in item or not isinstance(item["title"], str) or not item["title"].strip():
            raise ValueError(f"Элемент {i}: 'title' должен быть непустой строкой")

        # Проверка completed
        if "completed" not in item or type(item["completed"]) is not bool:
            raise ValueError(f"Элемент {i}: 'completed' должен быть логическим значением (bool)")


def completion_counts(todos):
    counts = {}
    for task in todos:
        uid = task["userId"]
        if uid not in counts:
            counts[uid] = 0
        if task["completed"]:
            counts[uid] += 1
    return counts


def top_users(counts):
    if not counts:
        return []
    max_val = max(counts.values())
    if max_val == 0:
        return []
    return sorted([uid for uid, count in counts.items() if count == max_val])


def select_tasks(todos, user_id, parameter=None):
    result = []
    for task in todos:
        if task["userId"] == user_id:
            if parameter is not None:
                if task["id"] <= parameter:
                    result.append(task["id"])
            else:
                result.append(task["id"])
    return result