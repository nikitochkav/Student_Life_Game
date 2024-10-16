import sys
from time import sleep

# Функция для печати текста с задержкой
def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()  # Для переноса строки после текста

# Главное меню
slow_print('Добро пожаловать в игру "Жизнь Игната"\n')
slow_print('Введите "start", чтобы начать игру, а "end", чтобы Игната отчислили еще до начала сессии\n')

# Обработка выбора пользователя
menu_choice = input().strip().lower()

if menu_choice == 'start':
    slow_print('Приключения Игната по сдаче зачёта начинаются\n')
elif menu_choice == 'end':
    slow_print('Bruh, Игната отчислили еще до начала сессии\n')
else:
    slow_print('Неверный ввод. Попробуйте снова.\n')
