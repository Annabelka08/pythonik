import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users, select_tasks


def read_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Ошибка: число должно быть положительным.")
        except ValueError:
            print("Ошибка: введите целое число.")


def read_non_negative_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            print("Ошибка: число должно быть неотрицательным.")
        except ValueError:
            print("Ошибка: введите целое число.")


def main():
    input_path = Path("todos.json")
    leaders_path = Path("leaders.json")
    selected_path = Path("selected.json")

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Ошибка: файл todos.json не найден.")
        return
    except UnicodeDecodeError:
        print("Ошибка: неверная кодировка файла (ожидается UTF-8).")
        return
    except json.JSONDecodeError as e:
        print(f"Ошибка формата JSON: {e}")
        return
    except OSError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return

    try:
        validate_todos(data)
    except ValueError as e:
        print(f"Ошибка структуры данных: {e}")
        return

    # Анализ
    counts = completion_counts(data)
    leaders = top_users(counts)

    print("=== Сводка ===")
    print(f"Количества выполненных задач по пользователям: {counts}")
    print(f"Лидеры (пользователи): {leaders}")

    # Сбор ID задач лидеров в исходном порядке
    leader_task_ids = [task["id"] for task in data if task["userId"] in leaders and task["completed"]]
    print(f"ID завершённых задач лидеров: {leader_task_ids}")

    # Индивидуальный вариант (Вариант 5)
    print("\n--- Индивидуальный вариант (5) ---")
    user_id = read_positive_int("Введите ID пользователя: ")
    threshold = read_non_negative_int("Введите порог для ID задачи (неотрицательное целое): ")

    selected_ids = select_tasks(data, user_id, parameter=threshold)
    print(f"Выбранные ID задач: {selected_ids}")

    # Сохранение результатов (только после успешной проверки!)
    try:
        with open(leaders_path, "w", encoding="utf-8") as f:
            json.dump(leader_task_ids, f, ensure_ascii=False, indent=2)
        with open(selected_path, "w", encoding="utf-8") as f:
            json.dump(selected_ids, f, ensure_ascii=False, indent=2)
        print(f"\nРезультаты успешно сохранены в {leaders_path} и {selected_path}")
    except OSError as e:
        print(f"Ошибка записи результатов: {e}")


if __name__ == "__main__":
    main()