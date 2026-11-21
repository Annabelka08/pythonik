import sys
from logic import add_record, find_records, set_completed, delete_record, statistics
from storage import load_records, save_records

DATA_FILE = "data.json"


def print_menu():
    print("\n--- План просмотра видеокурсов ---")
    print("1. Показать записи")
    print("2. Добавить курс")
    print("3. Найти курсы")
    print("4. Изменить статус")
    print("5. Удалить курс")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")
    print("----------------------------------")


def show_records(records):
    if not records:
        print("Нет записей.")
        return
    print(f"{'ID':<4} | {'Название курса':<25} | {'Категория':<15} | {'Уроков':<8} | {'Статус'}")
    print("-" * 75)
    for rec in sorted(records, key=lambda x: x["id"]):
        status = "Пройден" if rec["completed"] else "Не пройден"
        amount_str = f"{rec['amount']} ур."
        print(f"{rec['id']:<4} | {rec['title']:<25} | {rec['category']:<15} | {amount_str:<8} | {status}")


def get_valid_input(prompt, validator, error_msg):
    while True:
        val = input(prompt).strip()
        if validator(val):
            return val
        print(error_msg)


def get_non_empty(prompt):
    return get_valid_input(prompt, lambda x: len(x) > 0, "Поле не может быть пустым. Повторите ввод.")


def get_positive_int(prompt):
    return get_valid_input(prompt, lambda x: x.isdigit(), "Введите целое неотрицательное число.")


def main():
    try:
        records = load_records(DATA_FILE)
    except ValueError as e:
        print(f"Ошибка загрузки данных: {e}")
        sys.exit(1)

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_records(records)

        elif choice == "2":
            title = get_non_empty("Введите название видеокурса: ")
            category = get_non_empty("Введите категорию: ")
            amount_str = get_positive_int("Введите количество уроков: ")
            amount = int(amount_str)
            add_record(records, title, category, amount)
            print("Курс добавлен.")

        elif choice == "3":
            query = get_non_empty("Введите подстроку для поиска: ")
            found = find_records(records, query)
            if found:
                show_records(found)
            else:
                print("Ничего не найдено.")

        elif choice == "4":
            if not records:
                print("Список пуст.")
                continue
            show_records(records)
            id_str = input("Введите ID курса: ").strip()
            if not id_str.isdigit():
                print("Некорректный ID.")
                continue
            rec_id = int(id_str)
            ans = input("Отметить курс как пройденный? (да/нет): ").strip().lower()
            if ans in ("да", "нет"):
                completed = (ans == "да")
                if set_completed(records, rec_id, completed):
                    print("Статус изменён.")
                else:
                    print("Курс с таким ID не найден.")
            else:
                print("Отмена.")

        elif choice == "5":
            if not records:
                print("Список пуст.")
                continue
            show_records(records)
            id_str = input("Введите ID для удаления: ").strip()
            if not id_str.isdigit():
                print("Некорректный ID.")
                continue
            rec_id = int(id_str)
            confirm = input(f"Удалить курс {rec_id}? (да/нет): ").strip().lower()
            if confirm == "да":
                if delete_record(records, rec_id):
                    print("Курс удалён.")
                else:
                    print("Курс с таким ID не найден.")
            else:
                print("Удаление отменено.")

        elif choice == "6":
            stats = statistics(records)
            print(f"\nВсего курсов: {stats['total']}")
            print(f"Пройдено: {stats['completed']}")
            print(f"Не пройдено: {stats['not_completed']}")
            print(f"Общее количество уроков: {stats['total_amount']}")
            print("Уроки по категориям:")
            for cat, amt in stats['categories'].items():
                print(f"  {cat}: {amt} ур.")

        elif choice == "7":
            if save_records(DATA_FILE, records):
                print("Данные сохранены.")

        elif choice == "8":
            ans = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
            if ans == "да":
                if save_records(DATA_FILE, records):
                    print("Данные сохранены. Выход.")
                    break
                else:
                    print("Ошибка сохранения. Вы остаётесь в меню.")
            elif ans == "нет":
                print("Выход без сохранения.")
                break
            else:
                print("Повторите ввод.")

        else:
            print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()