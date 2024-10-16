import random as r

class Player:
    def __init__(self, hp, coins, damage):
        self.hp = hp
        self.coins = coins
        self.damage = damage

    def print_stats(self):
        print(f"У тебя {self.hp} жизней, {self.damage} урона и {self.coins} монет.")

    def print_hp(self):
        print(f"У тебя {self.hp} жизней.")

    def print_coins(self):
        print(f"У тебя {self.coins} монет.")

    def print_damage(self):
        print(f"У тебя {self.damage} урона.")

    def buy(self, cost):
        if self.coins >= cost:
            self.coins -= cost
            self.print_coins()
            return True
        print("У тебя маловато монет!")
        return False


class Monster:
    def __init__(self, level):
        self.level = level
        self.hp = level
        self.damage = level * 2 - 1
        self.name = r.choice(["Пьяный Игоря", "Clop", "Cholop", "Madrock", "Lilbitch"])

    def print_stats(self):
        print(f"Ты набрел на {self.name}, у него {self.level} уровень, {self.hp} жизней и {self.damage} урона.")


def meet_shop(player):
    weapon_lvl = r.randint(1, 3)
    weapon_dmg = r.randint(1, 5) * weapon_lvl
    weapons = ["Бутылка получше", "Меч из Майнкрафта", "Тяпка", "Цветочек с клумбы", 
               "Котлета из общего холодильника", "Аргумент"]
    weapon_rarities = ["Обычный(ая)", "Редкий(ая)", "Легендарный(ая)"]
    weapon_rarity = weapon_rarities[weapon_lvl - 1]
    weapon_cost = r.randint(300, 1000) * weapon_lvl
    weapon = r.choice(weapons)

    one_hp_cost = 500
    three_hp_cost = 1200

    print("""
============================================================================================================
На пути тебе встретился местный барыга Степан!

Он предлагает тебе ознакомиться с его ассортиментом
============================================================================================================
    """)
    player.print_stats()

    if input("""
    Что ты будешь делать: 
    1 - Давай показывай
    2 - Не, спасибо
""") == '1':
        print(f"""
============================================================================================================
1) Обед из Арены (+1HP) - {one_hp_cost} рублей
2) Шашлычок из Кавказского дворика (+3HP) - {three_hp_cost} рублей
3) {weapon_rarity} {weapon} (+{weapon_dmg} урона) - {weapon_cost} рублей
============================================================================================================
Что хочешь приобрести?""")
        choice = input()
        if choice == "1" and player.buy(one_hp_cost):
            player.hp += 1
            player.print_hp()
        elif choice == "2" and player.buy(three_hp_cost):
            player.hp += 3
            player.print_hp()
        elif choice == "3" and player.buy(weapon_cost):
            player.damage = weapon_dmg
            print('У тебя теперь новое оружие!')
            player.print_damage()


def meet_monster(player):
    monster = Monster(r.randint(1, 3))
    print("""
============================================================================================================
*музыка боя из Скайрима*
""")
    monster.print_stats()
    player.print_stats()

    while monster.hp > 0:
        choice = input("""
    1 - Биться
    2 - Сбежать
        """)

        if choice == "1":
            monster.hp -= player.damage
            print(f"Ты атаковал монстра, у него осталось {monster.hp} жизней.")
            if monster.hp > 0:
                player.hp -= monster.damage
                print(f"Монстр атаковал, у тебя осталось {player.hp} жизней.")
                if player.hp <= 0:
                    print("Ты проиграл.")
                    break
        elif choice == "2":
            if r.randint(0, monster.level) == 0:
                print("Тебе удалось сбежать!")
                break
        if monster.hp <= 0:
            loot = r.randint(0, 2) + monster.level
            player.coins += loot
            print(f"Ты победил монстра и получил {loot} монет.")
            player.print_coins()


def init_game():
    player = Player(3, 500, 1)
    print(f"""============================================================================================================
                                    Добро пожаловть в игру "Жизнь Игната"

На старте у вас есть:
Урон: {player.damage}
Жизни: {player.hp}
Деньги: {player.coins} рублей
============================================================================================================
""")
    return player


def game_loop(player):
    situation = r.randint(0, 10)
    if situation == 0:
        meet_shop(player)
    elif situation == 1:
        meet_monster(player)
    else:
        print("Блуждаем по колледжу...\n")


player = init_game()

while player.hp > 0:
    game_loop(player)
    if player.hp <= 0:
        if input("Хотите попробовать ещё раз? 1 - Да 2 - Нет\n") == "1":
            player = init_game()
        else:
            print("Счастья здоровья!")
            break
