# Лабораторная работа: JSON, анализ данных и HTTP-запросы

## Структура проекта
- `todos.json` — исходные данные.
- `analysis.py` — функции валидации и анализа.
- `main.py` — основная программа чтения, анализа и сохранения.
- `fetch_profile.py` — получение профиля GitHub (сеть или локально).
- `test_analysis.py` — модульные тесты.

## Команды запуска
```bash
python main.py                 # Основной анализ и сохранение leaders.json, selected.json
python fetch_profile.py        # Запрос профиля GitHub (с меню выбора источника)
python -m unittest test_analysis.py  # Запуск проверок
