# Игра "Жизнь Игната": Приключение Студента

Добро пожаловать в репозиторий игры **"Жизнь Игната"** — интерактивного приключения, где игроку предстоит помочь обычному студенту Игнату пройти через череду случайных событий, включая встречи с монстрами, барыгами и даже сложные зачёты. Игра разработана на Python с использованием базовых модулей для интерактивного геймплея.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Функциональность](#функциональность)
- [Тестирование](#тестирование)
- [Структура проекта](#структура-проекта)
- [Авторы](#авторы)
- [Лицензия](#лицензия)

## Установка

1. **Клонирование репозитория:**

    ```bash
    git clone https://github.com/your-repo/Student_Life_Game.git
    ```

2. **Создание и активация виртуального окружения:**

    Для Linux/macOS:
    ```bash
    cd Student_Life_Game
    python3 -m venv venv
    source venv/bin/activate
    ```

    Для Windows:
    ```bash
    cd IgnatLife
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Установка зависимостей:**

    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. **Запуск игры:**

    После установки всех зависимостей, запустите игру следующей командой:

    ```bash
    python main.py
    ```

2. **Начало приключений:**

    Игроку предложат два варианта:
    - Введите `"start"` для начала игры.
    - Введите `"end"`, чтобы завершить игру, не начав её.

    В зависимости от случайных событий в игре, вы встретите монстров, барыг и другие неожиданные ситуации.

## Функциональность

- **Главное меню:** Простое меню для выбора начала игры или завершения до начала.
- **Рандомные события:** Игрок будет сталкиваться с монстрами, местными торговцами и другими непредсказуемыми ситуациями.
- **Система боя:** Встречаясь с монстрами, игрок решает, драться или попытаться сбежать.
- **Магазин:** Игрок может покупать предметы, восстанавливающие жизни или повышающие урон.
- **Параметры Игната:** У Игната есть показатели здоровья, урона и монет, которые влияют на исход игры.

## Тестирование

Для запуска тестов используйте следующую команду (если тесты предусмотрены):

```bash
pytest
