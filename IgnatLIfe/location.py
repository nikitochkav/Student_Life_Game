import time
import sys
import random as r


class IgnatGame:
    def __init__(self, hp=3, coins=500, damage=1):
        self.hp = hp
        self.coins = coins
        self.damage = damage
        self.listw = ['Катиковк', 'Соф', 'Лер', 'Диан']
        self.listm = ['Виталик', 'Никитосик', 'Баграт']

    def print_text_with_delay(self, text, delay=0.032):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def print_parameters(self):
        print(f"У тебя {self.hp} жизней, {self.damage} урона и {self.coins} монет.")

    def meet_shop(self):
        weapon_lvl = r.randint(1, 3)
        weapon_dmg = r.randint(1, 5) * weapon_lvl
        weapons = ["Бутылка получше", "Меч из Майнкрафта", "Тяпка", "Цветочек с клумбы", "Котлета из общего холодильника", "Аргумент"]
        weapon_rarities = ["Обычный(ая)", "Редкий(ая)", "Легендарный(ая)"]
        weapon_rarity = weapon_rarities[weapon_lvl - 1]
        weapon_cost = r.randint(300, 1000) * weapon_lvl
        weapon = r.choice(weapons)

        one_hp_cost = 500
        three_hp_cost = 1200

        self.print_text_with_delay("""
============================================================================================================
На пути тебе встретился местный барыга Степан!

Оооо Привет Игнат, как дела? Как жизнь молодая?
Ладно не суть. У меня тут для тебя кое-что припасено.
Будешь брать?

Он предлагает тебе ознакомиться с его ассортиментом
============================================================================================================
""")
        self.print_parameters()

        choice = input("""
    Что ты будешь делать: 
    1 - Давай показывай, солнышко
    2 - Не, спасибо
""")
        if choice == '1':
            self.print_text_with_delay(f"""
============================================================================================================
Степа распахивает свой длинный плащ и вы в ожидании чего-то особенного наклоняетесь посмотреть поближе

    Там оказывается:
    1) Обед из Арены(+1HP) - {one_hp_cost} рублей
    2) Шашлычок из Кавказского дворика(+3HP) - {three_hp_cost} рублей
    3) {weapon_rarity} {weapon}(+{weapon_dmg} урона) - {weapon_cost} рублей
============================================================================================================
""")
            choice = input("Что хочешь приобрести?")
            if choice == "1":
                if self.buy(one_hp_cost):
                    self.hp += 1
                    self.print_parameters()
            elif choice == "2":
                if self.buy(three_hp_cost):
                    self.hp += 3
                    self.print_parameters()
            elif choice == "3":
                if self.buy(weapon_cost):
                    self.damage = weapon_dmg
                    self.print_parameters()
        else:
            self.print_text_with_delay("Вы отказались от покупок.")

    def buy(self, cost):
        if self.coins >= cost:
            self.coins -= cost
            self.print_parameters()
            return True
        self.print_text_with_delay("У тебя маловато монет!")
        return False

    def meet_monster(self):
        monster_lvl = r.randint(1, 3)
        monster_hp = monster_lvl
        monster_dmg = monster_lvl * 2 - 1
        monsters = ["Пьяного Игорька", "Кого-то из Деканата", "Шкилу из лицея", "Эго Игната", "Контрольную точку"]
        monster = r.choice(monsters)

        self.print_text_with_delay(f"""
============================================================================================================
Ты набрел на {monster}, у него {monster_lvl} уровень, {monster_hp} жизней и {monster_dmg} урона.
Придется драться

*музыка боя из Скайрима*
============================================================================================================
""")
        self.print_parameters()

        while monster_hp > 0:
            choice = input("""
    Что будешь делать?
    1 - Биться как мужик, я же Игнат
    2 - Сбегу как попуск, я слабенький
""")
            if choice == "1":
                monster_hp -= self.damage
                print(f"Ты атаковал, у него осталось {monster_hp} жизней.")
            elif choice == "2":
                if r.randint(0, monster_lvl) == 0:
                    self.print_text_with_delay("Тебе удалось сбежать с поля боя!")
                    break
                else:
                    self.print_text_with_delay("Оно догнало тебя!")

            if monster_hp > 0:
                self.hp -= monster_dmg
                print(f"Оно атаковало, у тебя {self.hp} жизней осталось.")
                if self.hp <= 0:
                    self.print_text_with_delay("Игнат был побежден!")
                    break
            else:
                loot = r.randint(0, 2) + monster_lvl
                self.coins += loot
                print(f"Ты победил {monster}, получив {loot} монет.")
                self.print_parameters()

    def event_handler(self):
        situation = r.randint(0, 4)
        if situation == 0:
            self.meet_shop()
        elif situation == 1:
            self.meet_monster()
        else:
            print("Пока ничего не произошло...")

    def start_game(self):
        self.print_text_with_delay("""
============================================================================================================
                                    Добро пожаловать в игру Жизнь Игната

            Это приключение обычного студента IT-колледжа Сириус по имени Игнат, который мечтает
                               не отчислиться в первом семестре после сессии

============================================================================================================
""")
        self.print_parameters()
        for _ in range(r.randint(10, 15)):
            self.event_handler()


game = IgnatGame()
game.start_game()
