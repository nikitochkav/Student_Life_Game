from time import sleep
import sys
menu = 'Добро пожаловать в игру "Жизнь Игната"\n'
for i in menu:
        sleep(0.026)
        sys.stdout.write(i)
        sys.stdout.flush()
start = 'Введите "start", чтобы начать игру, а "end", чтобы Игната отчислили еще до начала сессии \n'
for i in start:
        sleep(0.026)
        sys.stdout.write(i)
        sys.stdout.flush()
menu = input()
if menu == 'start':
    a = 'Приключения Игната по сдаче зачёта начинаются\n'
    for i in a:
        sleep(0.026)
        sys.stdout.write(i)
        sys.stdout.flush()
else:
    b = 'Bruh Игната отчислили еще до начала сессии\n'
    for i in b:
        sleep(0.026)
        sys.stdout.write(i)
        sys.stdout.flush()




