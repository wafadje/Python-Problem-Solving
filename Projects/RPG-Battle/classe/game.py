import random

class Colors:
    HEADER = '\033[33;1;4m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[33m'
    TITLE = '\033[1;43m'
    TITLE2 = '\033[1;95m'
    TITLE3 = '\033[1;91m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    TITLE4 = '\033[1;30;42m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name    # player name
        self.hp = hp    # hit points
        self.maxhp = hp
        self.mp = mp    # magic points
        self.maxmp = mp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df 
        self.magic = magic  
        self.items = items
		self.actions = ["Attack", "Magic", "Items"]


	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)

	def generate_spell_damage(self,i):
		ngl = self.magic[i]["dmg"] - 5 
		ngh = self.magic[i]["dmg"] + 5
		return random.randrange(ngl,ngh)

	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n " + Colors.TITLE + " ACTIONS " + Colors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n " + Colors.TITLE2 + " MAGIC " + Colors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:",  spell.cost, ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n " + Colors.TITLE3 + " ITEMS " + Colors.ENDC)
        for item in self.items:
            print("    " + str(i) + "." + item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp/self.maxhp) * 100 / 2.6

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 39:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            hp_decreased = 9 - len(hp_string)

            while hp_decreased > 0:
                current_hp += " "
                hp_decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print(Colors.FAIL + str(self.name) + "        " +Colors.FAIL + current_hp + " |" + hp_bar + "| " + Colors.ENDC)

    def get_stats(self):

        hp_bar = ""
        hp_bar_ticks = (self.hp/self.maxhp) * 100 / 4

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar = ""
        mp_bar_ticks = (self.mp/self.maxmp) * 100 / 10

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            hp_decreased = 9 - len(hp_string)

            while hp_decreased > 0:
                current_hp += " "
                hp_decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            mp_decreased = 7 - len(mp_string)

            while mp_decreased > 0:
                current_mp += " "
                mp_decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print(Colors.OKYELLOW + str(self.name) + "        "
              + Colors.OKGREEN + current_hp + " |" + hp_bar + "| "
              + Colors.OKBLUE + current_mp + " |" + mp_bar + "| "
              + Colors.ENDC)


    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]


    def choose_target(self, enemies):
        i = 1
        print("\n " + Colors.TITLE + " Enemies " + Colors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ":", enemy.name)
                i += 1

        choice = int(input("Choose Enemy:")) - 1
        return choice

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100
        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            spell, magic_dmg = self.choose_enemy_spell()

        return spell, magic_dmg
