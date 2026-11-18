import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def fetch_profile_network(login):
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def fetch_profile_local():
    local_path = Path("profile_sample.json")
    if not local_path.exists():
        # Создаём учебный файл, если его нет
        local_path.write_text('{"login": "demo", "id": 1, "name": null}', encoding="utf-8")

    with open(local_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def print_profile(data):
    print("\n--- Профиль пользователя ---")
    print(f"Логин: {data.get('login')}")
    print(f"ID: {data.get('id')}")
    print(f"Имя: {data.get('name')}")
    print("--------------------------\n")


def main():
    print("Выберите источник данных:")
    print("1. Сеть (GitHub API)")
    print("2. Локальный учебный пример")
    choice = input("Ваш выбор (1/2): ").strip()

    try:
        if choice == "1":
            login = input("Логин GitHub: ")
            data = fetch_profile_network(login)
            print(f"Профиль успешно получен из сети: {data['login']}")
        elif choice == "2":
            print("Используются учебные локальные данные.")
            data = fetch_profile_local()
            print(f"Профиль успешно прочитан локально: {data['login']}")
        else:
            print("Неверный выбор.")
            return

        print_profile(data)

        # Сохранение результата
        output = Path(__file__).resolve().parent / "profile.json"
        with open(output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"Профиль также сохранён в {output}")

    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()