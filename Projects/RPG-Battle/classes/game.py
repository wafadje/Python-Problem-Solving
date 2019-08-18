import random

class Colors():
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


# create player class
class Person:
    # define the player parameters
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name    # player name
        self.hp = hp    # hit points
        self.maxhp = hp
        self.mp = mp    # magic points
        self.maxmp = mp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df    # defence points
        self.magic = magic    # magics abilities
        self.items = items
		self.actions = ["Attack", "Magic", "Items"]


	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)


		
